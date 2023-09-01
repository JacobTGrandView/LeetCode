# Write your MySQL query statement below
select customer_id, COUNT(visits.visit_id) as count_no_trans
from Visits
left join transactions on visits.visit_id = transactions.visit_id #Left join is all records from left table and matching records from right table. #left join table2 on table1.column_name = table2.column_name
where transaction_id is null 
group by customer_id