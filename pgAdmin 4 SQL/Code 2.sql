SELECT 
    n.nspname AS schema_name,
    c.relname AS table_name,
    c.reltuples::bigint AS estimated_row_count
FROM 
    pg_class c
JOIN 
    pg_namespace n ON n.oid = c.relnamespace
WHERE 
    c.relkind = 'r'  -- Only include regular tables
    AND n.nspname NOT IN ('pg_catalog', 'information_schema')
ORDER BY 
    estimated_row_count DESC;
