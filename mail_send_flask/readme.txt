SEND MAIL USING FLASK AND GMAIL APP PASSWORD
In this article, we will learn about sending mail to our Gmail using flask and app password(Gmail).

What is an app password and why do we need it?

An App Password is a 16-digit passcode that gives a less secure app or device permission to access your Google Account. App Passwords can only be used with accounts that have 2-Step Verification turned on.

Steps to generate App password:

If you have enabled 2-Step-Verification and get a “smtplib.SMTPAuthenticationError” error when we try to send mail using flask-mail, we can try to use an App Password.

Go to your Google Account.
Select Security.

Select Security Tab
3. Under “Signing in to Google,” select App Passwords. You may need to sign in. If you don’t have this option, it might be because:

a) 2-Step Verification is not set up for your account.
b) 2-Step Verification is only set up for security keys.
c) Your account is through work, school, or other organizations.
d) You turned on Advanced Protection.


2-Step Verification is enabled
4. At the bottom, choose Select app and Select Other(Custom name), and enter the name of your app. Select the device(not mandatory) and choose the device you’re using and click on Generate.


5. Follow the instructions to enter the App Password. The App Password is the 16-character code in the yellow bar on your device.


16-digit App password window
Now we are all set to use this App password.

Note: Most of the time, you’ll only have to enter an App Password once per app or device, so don’t worry about memorizing it.

Let’s use this password in our app

