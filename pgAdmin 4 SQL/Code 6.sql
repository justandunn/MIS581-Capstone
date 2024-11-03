SELECT
    tc.table_schema,
    tc.table_name,
    kcu.column_name AS key_column,
    tc.constraint_type
FROM
    information_schema.table_constraints AS tc
JOIN
    information_schema.key_column_usage AS kcu 
    ON tc.constraint_name = kcu.constraint_name
    AND tc.table_schema = kcu.table_schema
WHERE
    tc.table_schema IN ('int', 'public', 'raw', 'rpt')
    AND tc.constraint_type IN ('PRIMARY KEY', 'FOREIGN KEY')
ORDER BY
    tc.table_schema, tc.table_name, constraint_type;
