The mechworker.py script can be used to drive webpage load.

Syntax: mechworker.py 200 mails.csv http://example.com/mw.html
runs concurrent 200 threads post to the page specified in the parameter for all the entries in mails.csv

The page has first name, last name and e-mail on it. It is a basic contact form.

The script uses python2 and the mechanize module

The makemails script can be used to build the mails.csv file.

Suyntax: makemails.py 30 40 example.com

creates a mails.csv suitable for the consumption of the mechworker.py program

example:

	U30,Userslastname,U30@example.com
	U31,Userslastname,U31@example.com
	U32,Userslastname,U32@example.com
	U33,Userslastname,U33@example.com
	U34,Userslastname,U34@example.com
	U35,Userslastname,U35@example.com
	U36,Userslastname,U36@example.com
	U37,Userslastname,U37@example.com
	U38,Userslastname,U38@example.com
	U39,Userslastname,U39@example.com

Sample: mw.html file

	<HTML>
	<BODY>
	<FORM ACTION=/cgi-bin/ignore.cgi>
	<h3>Contact Form</h3>
	First Name:<INPUT NAME=FirstName TYPE="text">
	<br>
	Last Name:<INPUT NAME=LastName TYPE="text">
	<br>
	E-mail:<INPUT NAME=Email TYPE="text">
	<br>
	<br>
	<INPUT TYPE="submit" VALUE"=Submit">
	<br>
	<br>
	</FORM>
	</BODY>
	</HTML>
