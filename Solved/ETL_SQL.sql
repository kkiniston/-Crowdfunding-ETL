-- Challenge Bonus queries.
-- 1. (2 pts)
-- Retrieve the number of backer_counts in descending order for each `cf_id` for only "live" campaigns. 


SELECT cf_id, backers_count
FROM campaign
WHERE outcome = 'live'
ORDER BY backers_count DESC;


-- 2. (2 pts)
-- Using the "backers" table confirm the results in the first query.

SELECT cf_id, COUNT(backer_id) AS "Total Backers"
FROM backers
GROUP BY cf_id
ORDER BY "Total Backers" DESC;

-- 3. (4 pts)
-- Create a table, "email_contacts_remaining_goal_amount", that has the first and last name, and email address of each contact.
-- And, the amount left to reach the goal for all "live" projects in descending order. 

SELECT CN.first_name, 
       CN.last_name, 
       CN.email, 
       (CP.goal-CP.pledged) AS "Remaining Goal Amount"
INTO email_contacts_remaining_goal_amount
FROM contacts as CN
JOIN campaign as CP
ON CP.contact_id = CN.contact_id
WHERE CP.outcome = 'live'
ORDER BY "Remaining Goal Amount" DESC;

-- Check the table

SELECT * FROM email_contacts_remaining_goal_amount;

-- 4. (7 pts)
-- Create a table, "email_backers_remaining_goal_amount" that contains the email address of each backer in descending order, 
-- and has the first and last name of each backer, the cf_id, company name, description, 
-- end date of the campaign, and the remaining amount of the campaign goal as "Left of Goal". 

SELECT BK.email,
       BK.first_name, 
       BK.last_name, 
       BK.cf_id, 
       CP.company_name,
       CP.description,
       CP.end_date,
       (CP.goal-CP.pledged) as "Left of Goal"
INTO email_backers_remaining_goal_amount
FROM campaign as CP
LEFT JOIN backers as BK
ON CP.cf_id = BK.cf_id
WHERE CP.outcome = 'live'
GROUP BY BK.email,
       BK.first_name, 
       BK.last_name,
       BK.cf_id, 
       CP.company_name,
       CP.description,
       CP.end_date,
       "Left of Goal"
ORDER BY BK.last_name;

-- Check the table

SELECT * FROM email_backers_remaining_goal_amount;


