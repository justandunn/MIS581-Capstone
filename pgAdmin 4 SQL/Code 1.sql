SELECT 
    table_schema,
    table_name,
    column_name,
    data_type,
    is_nullable,
    character_maximum_length,
    numeric_precision,
    numeric_scale
FROM 
    information_schema.columns
WHERE 
    table_schema IN ('int', 'public', 'raw', 'rpt')
ORDER BY 
    table_schema, table_name, ordinal_position;
