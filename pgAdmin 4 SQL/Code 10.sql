-- Query to list column names and data types
SELECT 
    column_name, 
    data_type
FROM 
    information_schema.columns
WHERE 
    table_schema = 'public' 
    AND table_name = 'treasury_appropriation_account';

-- Query to retrieve the first 20 rows
SELECT *
FROM 
    public.treasury_appropriation_account
LIMIT 20;
