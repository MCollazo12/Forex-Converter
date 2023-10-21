### Conceptual Exercise
  
Answer the following questions below:
- What are important differences between Python and JavaScript?


>> Python is typically executed on the server side or in scripts, whereas JavaScript is
primarily a client side language that is executed in a web browser. Likewise, Python is an authentic
OOP language that uses a class-based inheritance structure. While JavaScript supports 
inheritance, it depends on a 'software prototype-based model'. Python is considered a
strongly-typed language, whereas JavaScript is a weakly-typed language.
        

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.


>>1. Using the dictionary's 'get' method which returns a specified default value
    rather than raising a 'KeyError'.
>>2. Using an if statement to check whether the key exists within the dictionary.
    If the key doesn't exist, return a specified default value.


- What is a unit test?
        
>>A unit test describes testing the smallest piece of code that can be isolated
within a program (function, method, property, etc.)

- What is an integration test?


>>An integration test takes a unit test a step further and specifically tests compon$
of a program that are meant to work together.
        

- What is the role of web application framework, like Flask?


>>A web application framework simplifies and supports the process of building
and running web applications.
        

- You can pass information to Flask either as a parameter in a route URL 
(like '/foods/pretzel') or using a URL query param (like
'foods?type=pretzel'). How might you choose which one is a better fit
for an application?


>>Using URL route parameters allows for clean, semantic URLs. Route parameters
also allow the URL to represent different levels of hierarchical
structure for a page (ex. /category/product).      
>>On the other hand, URL query parameters allow for increased user flexibility
when customizing queries (optional/multiple parameters, filtering, sorting,etc.) 
without changing the base URL.
        

- How do you collect data from a URL placeholder parameter using Flask?


>>Data can be colleted from a URL placeholder parameter by passing the
paramter value to the view function as an argument.
        

- How do you collect data from the query string using Flask?


>>Query string data can be collected by importing and using the 'request'
object. By using 'request.args' within a view function, the URL query
parameters can be accessed.


- How do you collect data from the body of the request using Flask?


>>The 'request' object can be used again to collect data from the body
of the request. The method for collecting this data depends on the content
type of the request ('request.get_json()' for JSON data and 'request.form'
for form data).


- What is a cookie and what kinds of things are they commonly used for?


>>A cookie is a piece of data that a web server sends to a user's browser.
This data is stored locally on the user's machine and usually contains
settings and information related to the user's interaction with a website.
Cookies are commonly used for user authentication, personalization, analytics,
tracking user sessions, and storing user preferences.


- What is the session object in Flask?


>The session is an object within Flask that is used to store/maintain user-specific
data across multiple requests on the webpage. 


- What does Flask's `jsonify()` do?


>Flask's jsonify function is a utility that simplifies the JSON response process
from a Flask route. jsonify() takes in dictionaries/lists and converts them into
a JSON formatted response that can then be sent back to the client's browser.