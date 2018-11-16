monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "February",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
#use curly brackets
print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get("mon","that's not a valid entry")) #pass a default response for non valid entry