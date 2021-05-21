This is a simple python script, made during my GATE days, primarily to monitor important changes on institute webpages for any important announcements, declaration of results etc. It can monitor any number of urls at once, hence you dont have to keep checking / refreshing the webpages (I know how annoying that can get xD)

This will directly notify the user if any changes happen in the content of the webpage via email.

How to Use? (Setup time: ETA 5mins)


1. Pull this repo locally in any folder
2. In the file "urls.txt", add the urls you want to monitor just as mentioned in the file
3. In the file "ids.txt", add the email ids you want to notify
4. In the file "credentials.txt" add your gmail (This is the email which will be sending the mail notification, it HAS to be GMAIL)username, and password - don't worry, you will be running it locally, so no one is going to see them :D
5. Gmail, by default blocks logins via scripts, you can change that by following simple steps mentioned here: https://tinyurl.com/58pzhyuh

6. Just run script using command `python3 helper.py` 

TIP: Keep the script running in the background in the time window, whenever you feel anything important may be released

Any doubts, feel free to reach out-

LinkedIn: https://www.linkedin.com/in/varadkulkarni11
Email: varadvinodkulkarni@gmail.com
