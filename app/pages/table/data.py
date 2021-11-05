from configparser import ConfigParser
from werkzeug4py.db import DataLoader
from werkzeug4py.plotting import colors
import pandas as pd
from pathlib import Path

config = ConfigParser()
config.read('config.ini')

DATA_FOLDER: Path = Path(config.get('data', 'data_folder'))
SQL_FOLDER: Path = Path(config.get('data', 'sql_folder'))
DAWIS_DEPENDENCIES: Path = Path(config.get('data', 'dawis_dependencies'))
DATA: Path = Path('test')


def load_pickle():

    # load data from pickle
    data = pd.read_pickle(
        DATA_FOLDER / DATA.with_suffix('.pkl'))

    return data


def load_db():
    # load data from DB
    dawis = DataLoader(driver='db2', database='dawisp')
    dawis_dependencies = dawis.data_load(
        sql=SQL_FOLDER / DAWIS_DEPENDENCIES.with_suffix('.sql'),
        local=DATA_FOLDER / DAWIS_DEPENDENCIES.with_suffix('.pkl')
    )
    return dawis_dependencies
