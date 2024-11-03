SELECT table_schema, table_name, column_name,
       100.0 * SUM(CASE WHEN column_name IS NULL THEN 1 ELSE 0 END) / COUNT(*) AS null_percentage
FROM information_schema.columns
GROUP BY table_schema, table_name, column_name;
