SELECT c.table_schema, 
       c.table_name, 
       COUNT(*) AS row_count
FROM information_schema.columns AS c
JOIN information_schema.tables AS t ON c.table_name = t.table_name 
    AND c.table_schema = t.table_schema
GROUP BY c.table_schema, c.table_name
ORDER BY c.table_schema, c.table_name;
