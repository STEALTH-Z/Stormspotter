CREATE_INDEX_CYPHER_LIST = [
    "CREATE INDEX IF NOT EXISTS FOR (n:AADOBJECT) ON (n.objectid)",
    "CREATE INDEX IF NOT EXISTS FOR (n:AADUSER) ON (n.userprincipalname);",
    "CREATE INDEX IF NOT EXISTS FOR (n:ARMRESOURCE) ON (n.name);",
    "CREATE INDEX IF NOT EXISTS FOR (n:RESOURCEGROUP) on (n.resourcegroupname);",
    "CREATE INDEX IF NOT EXISTS FOR (s:SUBSCRIPTION) ON (s.name);",
]
