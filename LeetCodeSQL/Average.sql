# Write your MySQL query statement below
select
ROUND(sum(item_count*order_occurrences)/sum(order_occurrences),2) as average_items_per_order
from Orders