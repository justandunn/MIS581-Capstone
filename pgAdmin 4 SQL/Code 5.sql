SELECT n.nspname AS schema_name,
       c.relname AS table_name,
       c.reltuples::bigint AS approximate_row_count
FROM pg_class c
JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE c.relkind = 'r'
  AND n.nspname IN ('int', 'public', 'raw', 'rpt')
ORDER BY schema_name, table_name;
