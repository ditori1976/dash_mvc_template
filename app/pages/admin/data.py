# %%
from configparser import ConfigParser
from numpy import pi
from werkzeug4py.db import DataLoader
from werkzeug4py.plotting import colors
import pandas as pd
from friss.pipeline import main as pipeline
from pathlib import Path

config = ConfigParser()
config.read('config.ini')

SQL_FOLDER: Path = Path(config.get('data', 'sql'))
DATA: Path = Path(config.get('data', 'data'))
DAWIS_DEPENDENCIES: Path = Path(config.get('sql', 'dawis_dependencies'))
PIPELINE_NETWORK: str = config.get('data', 'pipeline_network')

# DB2 Object Types
object_types = {'T': 'table',
                'V': 'view',
                'W': 'system_time period',
                'Z': 'business_time period',
                'F': 'function',
                'G': 'global temporary table',
                'M': 'materialized query table'}


def load_data():
    # run pipeline
    pipeline()
    pipeline_network = pd.read_pickle(
        (DATA / PIPELINE_NETWORK).with_suffix('.pkl'))
    # load DAWIS dependencies
    dawis = DataLoader(driver='db2', database='dawisp')
    dawis_dependencies = dawis.data_load(
        sql=SQL_FOLDER / DAWIS_DEPENDENCIES.with_suffix('.sql'),
        local=DATA / DAWIS_DEPENDENCIES.with_suffix('.pkl')
    )
    return pipeline_network, dawis_dependencies


# %%
pipeline_network, dawis_dependencies = load_data()

# %%
# add parent table from dawis dependencies and get type (view/table)
types = []
parents = []
for i, row in pipeline_network.iterrows():
    # pipeline_network.iloc[i]['Type'] =

    search = dawis_dependencies.loc[(dawis_dependencies['CHILD'] == row['Table']) & (
        dawis_dependencies['SCHEMA_CHILD'] == row['Schema']), :]
    types.append(search['TYPE_CHILD'].values[0])
    if search['CREATOR'].values[0]:
        parent = search['CREATOR'].values[0] + '.' + search['PARENT'].values[0]
    else:
        parent = row['Schema']
    parents.append(parent)
pipeline_network['Type'] = types
pipeline_network['Parent'] = parents
# %%
# create parent - child pairs for network analysis
# TODO: add attribute


def create_edges_nodes(df: pd.DataFrame, chain: list) -> dict:
    # TODO: integrate Type/Schema/Source in colors/shape

    edges = []
    nodes = set()

    def node_color(node):
        if node in pipeline_network['Script'].values:
            return colors[0]
        elif node in pipeline_network['Table'].values:
            return colors[1]
        elif node in pipeline_network['Schema'].values:
            return colors[2]
        elif node in pipeline_network['Source'].values:
            return colors[3]
        else:
            return colors[4]

    for i in range(0, len(chain) - 1):
        # all pairs in chain
        pairs = df.groupby([chain[i], chain[i + 1]]).first().index
        # all nodes in network
        nodes = nodes | set(df[chain[i]]) | set(
            df[chain[i + 1]])
        # dict with all edges (for visdcc)
        edges = edges + [
            {
                'id': f'{r[0]}_{r[1]}',
                'from': r[0],
                'to':r[1],
                'arrows':'to',
                'length':190
            }
            for r in pairs]
    # dict with all nodes (for visdcc)
    nodes = [{'id': node_name, 'label': node_name, 'shape': 'dot', 'color': node_color(node_name)}
             for node_name in nodes]

    return edges, nodes


# create extra path for parent
# TODO: more generic solution
chain_main = ['Source', 'Schema', 'Table', 'Script']  # , 'Attribute'
edges, nodes = create_edges_nodes(pipeline_network, chain_main)
chain_parents = ['Parent', 'Table', ]  # , 'Attribute'
edges_p, nodes_p = create_edges_nodes(pipeline_network, chain_parents)

edges = edges + edges_p
edges = [dict(s) for s in set(frozenset(d.items()) for d in edges)]
nodes = nodes + nodes_p
nodes = [dict(s) for s in set(frozenset(d.items()) for d in nodes)]
# %%
