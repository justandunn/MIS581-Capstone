-- Example relationships in 'public' schema
ALTER TABLE public.agency
ADD CONSTRAINT fk_agency_subtier
FOREIGN KEY (subtier_agency_id) REFERENCES public.subtier_agency (subtier_agency_id);

ALTER TABLE public.agency
ADD CONSTRAINT fk_agency_toptier
FOREIGN KEY (toptier_agency_id) REFERENCES public.toptier_agency (toptier_agency_id);

ALTER TABLE public.appropriation_account_balances
ADD CONSTRAINT fk_app_acc_balances_submission
FOREIGN KEY (submission_id) REFERENCES public.submission_attributes (submission_id);

ALTER TABLE public.appropriation_account_balances
ADD CONSTRAINT fk_app_acc_balances_treasury
FOREIGN KEY (treasury_account_identifier) REFERENCES public.treasury_appropriation_account (treasury_account_identifier);

-- Additional relationships for 'public.financial_accounts_by_awards'
ALTER TABLE public.financial_accounts_by_awards
ADD CONSTRAINT fk_fin_acc_awards_object_class
FOREIGN KEY (object_class_id) REFERENCES public.object_class (id);

ALTER TABLE public.financial_accounts_by_awards
ADD CONSTRAINT fk_fin_acc_awards_disaster
FOREIGN KEY (disaster_emergency_fund_code) REFERENCES public.disaster_emergency_fund_code (code);

ALTER TABLE public.financial_accounts_by_awards
ADD CONSTRAINT fk_fin_acc_awards_program_activity
FOREIGN KEY (program_activity_id) REFERENCES public.ref_program_activity (id);

ALTER TABLE public.financial_accounts_by_awards
ADD CONSTRAINT fk_fin_acc_awards_treasury
FOREIGN KEY (treasury_account_id) REFERENCES public.treasury_appropriation_account (treasury_account_identifier);

ALTER TABLE public.financial_accounts_by_awards
ADD CONSTRAINT fk_fin_acc_awards_submission
FOREIGN KEY (submission_id) REFERENCES public.submission_attributes (submission_id);
