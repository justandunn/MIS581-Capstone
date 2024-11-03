SELECT 
    taa.budget_function_title,
    taa.fr_entity_description,
    aab.reporting_period_end,
    aab.total_budgetary_resources_amount_cpe,
    aab.gross_outlay_amount_by_tas_cpe,
    aab.unobligated_balance_cpe,
    aab.status_of_budgetary_resources_total_cpe
FROM 
    public.treasury_appropriation_account AS taa
JOIN 
    public.appropriation_account_balances AS aab
ON 
    taa.treasury_account_identifier = aab.treasury_account_identifier
ORDER BY 
    aab.reporting_period_end DESC
LIMIT 20;
