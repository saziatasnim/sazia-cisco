# sazia-cisco

This web service responds to GET requests where the caller passes in a URL and the service responds with some information about that URL. 
I used Python for this assignment.
I used Virustotal API for the URL lookup.
Besides the .py file, I have created a .csv file that contains a list of URLs. You will need to install pandas module by "pip install pandas" in order to read .csv file.
Once the user runs the .py file after installing all the required modules, the program will ask for the file to read the URLs from; so you would need to enter the file name ("Malware.csv"). 
It will take few minutes to run the program and keep listing in the compiler if the URLs are safe or malicious. 
Once the test run is completed, it will create separate .txt files for "Clean", "Malicious" and "Not Found" URLs.



The answer of Part 2 questions are as follows:

• The size of the URL list could grow infinitely. How might you scale this beyond the memory capacity of the system?
    - We can use hard disk to store the data in files.

• Assume that the number of requests will exceed the capacity of a single system, describe how might you solve this, and how might this change if you have to distribute this workload to an additional region, such as Europe.
    - Using AWS cloud can solve this issue. Or create a secondary server and use load balancer.


• What are some strategies you might use to update the service with new URLs? Updates may be as much as 5 thousand URLs a day with updates arriving every 10 minutes.
    - Using REST API


• You’re woken up at 3am, what are some of the things you’ll look for?
    - In regards to the service, I may look if the server is still up and if the API is still providing the response.

• Does that change anything you’ve done in the app?
    - Probably not. I have set my sleep time to be 15 seconds in the service, which means in one minute it can take 4 requests. The service will not time out.

• What are some considerations for the lifecycle of the app?
    - Some things to consider are the size of the URL, number of requests as well as sleep time.
• You need to deploy a new version of this application. What would you do? 
    - One of the things I would do is use AWS or GCP cloud for the service. I would also prefer using C++ for better memory allocation.
