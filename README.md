# sazia-cisco

This web service responds to GET requests where the caller passes in a URL and the service responds with some information about that URL. 
I used Python for this assignment.
I used Virustotal API for the URL lookup.
Besides the .py file, I have created a .csv file that contains a list of URLs. You will need to install pandas module by "pip install pandas" in order to read .csv file.
Once the user runs the .py file after installing all the required modules, the program will ask for the file to read the URLs from; so you would need to enter the file name ("Malware.csv"). 
It will take few minutes to run the program and keep listing in the compiler if the URLs are safe or malicious. 
Once the test run is completed, it will create separate .txt files for "Clean", "Malicious" and "Not Found" URLs.
