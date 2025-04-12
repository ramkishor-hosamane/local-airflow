{{ config(
    schema='staging',
    materialized='table'
) }}

with stg as (
    select * from {{source('analytics','customers')}}
)
select * from stg
