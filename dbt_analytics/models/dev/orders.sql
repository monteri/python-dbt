{{ config(materialized="table") }}

select
    order_id,
    user_id,
    name,
    date as user_joined,
    order_date,
    total_amount
from {{ source("ws", "orders") }} o
left join {{ ref("users") }} u
on o.user_id = u.id