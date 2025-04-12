{{config(
    schema='staging',
    materialized='table')}}


select 

* 

from {{source('analytics','products')}}
