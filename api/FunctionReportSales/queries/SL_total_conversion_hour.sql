--------------------------------------------------------------------HOUR
SELECT
CASE WHEN SUB.NUM_SALES = 0 THEN CONCAT(0,'%')
							ELSE CONCAT(ROUND(((SUB.NUM_AMOUNT / SUB.NUM_SALES) * 100),2),'%')
END AS "Total hour conversion"
FROM
(
SELECT 
CAST(COUNT(PD.Amount) AS float) AS NUM_AMOUNT,
CAST(COUNT(BD.ReportID) AS float) AS NUM_SALES
FROM [dbo].[Policy_BrokersDetails] BD
LEFT JOIN [dbo].[Policy_PaymentDetails] PD
ON BD.ReportID = PD.ReportID
LEFT JOIN [dbo].[Company_Details] CD
ON BD.CompanyID = CD.CompanyID
LEFT JOIN [dbo].[UserProfile] UP
ON PD.LoggedBy = UP.UserId
WHERE
(BD.CompanyID IN ('71', '73','70','85','81','96','60','78','56','83','100','101')
	OR (BD.CompanyID IN ('63','86','108','53','92','102')
	AND BD.Funded <> 'yes'))
AND BD.LoggedDate > DATEADD(HOUR, -1, GETDATE())
) AS SUB