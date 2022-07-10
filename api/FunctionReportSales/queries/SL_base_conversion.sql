SELECT 
BD.ReportID,
CD.CompanyName,
CD.ClaimType,
BD.LoggedDate,
SUBSTRING(UP.Email,0,CHARINDEX('@',UP.Email)) AS "Name",
PD.LoggedDate AS "Sale Date",
PD.Amount
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
--AND CAST(BD.LoggedDate AS DATE) = CAST(GETDATE() AS DATE)
--AND BD.LoggedDate > DATEADD(HOUR, -1, GETDATE())
ORDER BY BD.LoggedDate
