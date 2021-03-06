# Generated by Django 2.2.13 on 2020-08-29 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0067_censussubdivision_pop_count_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='censussubdivision',
            name='low_income_status_0_to_17_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='low_income_status_0_to_17_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='low_income_status_18_to_64_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='low_income_status_18_to_64_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='low_income_status_65_and_over_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='low_income_status_65_and_over_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='median_total_income_f',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='median_total_income_m',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='naics_accomodation',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='naics_admin',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='naics_agriculture',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='naics_arts',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='naics_construction',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='naics_education',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='naics_finance',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='naics_healthcare',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='naics_information',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='naics_management',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='naics_manufacturing',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='naics_mining',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='naics_not_applicable',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='naics_other',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='naics_public_admin',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='naics_real_estate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='naics_retail',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='naics_tech',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='naics_transportation',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='naics_utilities',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='naics_wholesale',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='noc_0_management',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='noc_1_business_finance_admin',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='noc_2_natural_applied_sciences',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='noc_3_health',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='noc_4_education_law_social',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='noc_5_art_culture_sport',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='noc_6_sales',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='noc_7_trades_transport',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='noc_8_natural_resources_agriculture',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='noc_9_manufacturing',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='official_lang_both_eng_fr',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='official_lang_eng',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='official_lang_fr',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='official_lang_neither_eng_fr',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_0_4_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_0_4_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_100_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_100_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_10_14_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_10_14_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_15_19_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_15_19_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_20_24_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_20_24_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_25_29_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_25_29_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_30_34_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_30_34_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_35_39_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_35_39_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_40_44_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_40_44_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_45_49_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_45_49_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_50_54_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_50_54_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_55_59_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_55_59_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_5_9_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_5_9_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_60_64_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_60_64_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_65_69_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_65_69_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_70_74_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_70_74_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_75_79_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_75_79_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_80_84_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_80_84_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_85_89_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_85_89_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_90_94_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_90_94_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_95_99_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_95_99_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_count_0_14_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_count_0_14_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_count_14_65_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_count_14_65_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_count_65_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_count_65_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_count_total_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_count_total_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_pct_0_14_f',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_pct_0_14_m',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_pct_14_65_f',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_pct_14_65_m',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_pct_65_f',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='pop_pct_65_m',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='population_avg_age',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='population_density_per_sq_km',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_100000_to_149999_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_100000_to_149999_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_10000_to_19999_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_10000_to_19999_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_150000_and_over_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_150000_and_over_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_20000_to_29999_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_20000_to_29999_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_30000_to_39999_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_30000_to_39999_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_40000_to_49999_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_40000_to_49999_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_50000_to_59999_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_50000_to_59999_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_60000_to_69999_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_60000_to_69999_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_70000_to_79999_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_70000_to_79999_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_80000_to_89999_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_80000_to_89999_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_90000_to_99999_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_90000_to_99999_m',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_under_10000_f',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='censussubdivision',
            name='total_income_under_10000_m',
            field=models.IntegerField(null=True),
        ),
    ]
