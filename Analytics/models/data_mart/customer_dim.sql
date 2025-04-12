{{ config( schema='data_mart', 
    materialized='table'
)}}

with customer_dim as (
    select 
        customer_id,
        concat_ws(' ', first_name, last_name) as name,
        email,
        datediff(year, birthdate, current_date) as age,
        address
    from {{ ref('stg_customers') }}  -- Refers to the staging model
)

select * from customer_dim
