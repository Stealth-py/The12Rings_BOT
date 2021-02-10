This program extracts the user data from the leaderboard of The12Rings.

Firstly, you need to import the required modules, that is "requests" and "bs4"(for Beautiful Soup v4).
You will not need to install "requests" externally but for bs4, you need to type "pip install bs4" in your terminal to get the module installed.

We will be working on "https://www.the12rings.com", where we will first need to login using an account, and then go to the leaderboard to extract all of the table data, and check if the id entered by the user to the bot is the same as the id in the table and then proceed accordingly.

For the LOGIN part:
The link will become "https://www.the12rings.com/login", then we will make a credentials dictionary which we will use to store our login credentials and also push to the site, to enter.
We will need to create a session for this using "requests" module, or else all of it will be stored in cache and will be lost as soon as we are logged in.
After creating a session, we push the "credentials" to that "url" which allows us to access the website.

For the LEADERBOARD part:
The link now will become, "https://www.the12rings.com/leaderboard", and then we will extract the source code and store it in a variable, which we will need to use to initialise the BeautifulSoup object and parse it to html.
Afterwards, the for loop iterates through the source code, and as soon as it finds the "{"id": "tableData"}" attribute, it starts storing the data in a variable.
After stripping off the unnecessary part like, '<div id="tableData" style="display:none;">[' and ']</div>', we write this "text" to the file we created to store the leaderboard table data.
Now, we convert all this data to "dictionaries" and then store them as "strings", which will later on be used by, python's "eval()" function to be used as "dictionaries" in the code, which will be helpful to get the user id and the level of that user.
Afterwards, we iterate through these "strings" and convert them to dictionaries, and use the "id" as the key, to check if the 'user["id"]' is the same as the "usr_id" entered by the user.
If match is found, we update the "lvl" variable to the level of the user, and print to the IDE about the same.
If match is NOT found, we let the "lvl" variable unchanged with the value "0", which will be used later on in the main code, for error handling.

Returning the "lvl" would provide us with the level of the user with that specific user id.
