# moto manual

Just add the @mock_aws decorator to the function you want to mock boto3<br>
You can create virtual AWS service resources locally<br><br>
Prepare separate test code from the code you want to test. In the test code, set up the mocks, and call the code you want to test from the test code<br>
The code you want to test can be tested without making any changes