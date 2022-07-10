----------------------------------------------------------------BY SALER DAY
SELECT 
SUBSTRING(UP.Email,0,CHARINDEX('@',UP.Email)) AS "Name",
COUNT(PD.Amount) AS "No",
SUM(PD.Amount) AS Amount
FROM [dbo].[Policy_PaymentDetails] PD
LEFT JOIN [dbo].[UserProfile] UP
ON PD.LoggedBy = UP.UserId
WHERE CAST(PD.LoggedDate AS DATE) = CAST(GETDATE() AS DATE)
GROUP BY UP.Email
ORDER BY SUM(PD.Amount) DESC;