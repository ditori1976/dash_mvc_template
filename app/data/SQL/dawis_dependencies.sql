with dep_schemas as (
    select 'o' as SCHEMA_CHILD,
        replace(CREATOR, ' ', '') as CHILD,
        'o' AS TYPE_CHILD,
        replace(CREATOR, ' ', '') as CREATOR,
        replace(NAME, ' ', '') as PARENT,
        replace(TYPE, ' ', '') as TYPE_PARENT
    from SYSIBM.SYSTABLES
),
dep_sysviewdep as (
    select replace(DCREATOR, ' ', '') as SCHEMA_CHILD,
        replace(DNAME, ' ', '') as CHILD,
        replace(DTYPE, ' ', '') as TYPE_CHILD,
        replace(BCREATOR, ' ', '') as CREATOR,
        replace(BNAME, ' ', '') as PARENT,
        replace(BTYPE, ' ', '') as TYPE_PARENT
    from SYSIBM.SYSVIEWDEP
),
nodes_systables as (
    select replace(CREATOR, ' ', '') as SCHEMA_CHILD,
        replace(NAME, ' ', '') as CHILD,
        replace(TYPE, ' ', '') AS TYPE_CHILD,
        null as CREATOR,
        null as PARENT,
        null as TYPE_PARENT
    from SYSIBM.SYSTABLES
),
nodes_sysviewdep_1 as (
    select replace(BCREATOR, ' ', '') as SCHEMA_CHILD,
        replace(BNAME, ' ', '') as CHILD,
        replace(BTYPE, ' ', '') as TYPE_CHILD,
        null as CREATOR,
        null as PARENT,
        null as TYPE_PARENT
    from SYSIBM.SYSVIEWDEP
),
nodes_sysviewdep_2 as (
    select replace(DCREATOR, ' ', '') as SCHEMA_CHILD,
        replace(DNAME, ' ', '') as CHILD,
        replace(DTYPE, ' ', '') as TYPE_CHILD,
        null as CREATOR,
        null as PARENT,
        null as TYPE_PARENT
    from SYSIBM.SYSVIEWDEP
),
nodes as (
    (
        select *
        from nodes_systables
    )
    union
    (
        select *
        from nodes_sysviewdep_1
    )
    union
    (
        select *
        from nodes_sysviewdep_2
    )
),
dependencies as (
    (
        select *
        from dep_schemas
    )
    union
    (
        select *
        from dep_sysviewdep
    )
),
output as (
    (
        select *
        from nodes
    )
    union all
    (
        select *
        from dependencies
    )
)
select *
from output;