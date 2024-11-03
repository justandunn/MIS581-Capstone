SELECT ta.budget_function_title,
       ta.fr_entity_description,
       ab.reporting_period_end,
       ab.total_budgetary_resources_amount_cpe,
       ab.gross_outlay_amount_by_tas_cpe,
       ab.unobligated_balance_cpe,
       ab.status_of_budgetary_resources_total_cpe,
       CASE 
           WHEN EXTRACT(YEAR FROM ab.reporting_period_end) IN (2013, 2014, 2016, 2018, 2021, 2022, 2023)
               THEN 'Omnibus'
           ELSE 'Non-Omnibus'
       END AS omnibus_flag
FROM public.treasury_appropriation_account AS ta
JOIN public.appropriation_account_balances AS ab
ON ta.treasury_account_identifier = ab.treasury_account_identifier
ORDER BY ab.reporting_period_end
LIMIT 20;
