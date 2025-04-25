select *
from {{ source("ws", "users") }}