{{ config(
    materialized='table'
) }}

with raw as (
  select *
  from 's3://uploads/Amazon Sale Report.csv'
),

parsed as (
  select
    -- string identifiers
    raw."Order ID"                             as order_id,
    CAST("Date" AS DATE)                       as sale_date,
    raw."Status"                               as status,
    raw."Fulfilment"                           as fulfilment,
    raw."Sales Channel"                        as sales_channel,
    raw."ship-service-level"                   as ship_service_level,
    raw."Style"                                as style,
    raw."SKU"                                  as sku,
    raw."Category"                             as category,
    raw."Size"                                 as size,
    raw."ASIN"                                 as asin,
    raw."Courier Status"                       as courier_status,

    -- numeric conversions
    try_cast(raw."Qty"           as integer)   as qty,
    raw."currency"                             as currency,
    try_cast(raw."Amount"        as double)    as amount,

    -- shipping geography
    raw."ship-city"                            as ship_city,
    raw."ship-state"                           as ship_state,
    try_cast(raw."ship-postal-code" as integer) as ship_postal_code,
    raw."ship-country"                         as ship_country,

    -- promotion and fulfillment flags
    raw."promotion-ids"                        as promotion_ids,
    raw."B2B"                                  as b2b,
    raw."fulfilled-by"                         as fulfilled_by

    -- drop raw.index and raw."Unnamed: 22"
  from raw
)

select * from parsed