-- tests/age_greater_than_70.sql
select *
from {{ ref('customer_dim') }}
where age > 70
