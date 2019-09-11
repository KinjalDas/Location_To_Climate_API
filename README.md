# Location_To_Climate_API

This API is used for converting location name as a string to the respective locality's weather data. Import module main from package LocationToWeatherAPI. Call main.driver(place,date="<date in string format>",type_of_forecast="<Any one from 1 to 4 in string format>"). You can pass ANY ONE OF the keyword arguments - Date in "YYYY-MM-DD" format/ forecast type required ('1' for today {Default Selection}, '2' for monthly,'3' for 5-day and '4' for 10-day). We are relying on APIs used by weather.com internally for extracting the respective data.

For ex:<br/>

1.If you just want today's weather metrics with place name: <br/>

from LocationToWeatherAPI import main<br/>
main.driver("Place-Name")<br/>

2.If you just want the current month's forecast with place name: <br/>

from LocationToWeatherAPI import main<br/>
main.driver("Place-Name",type_of_forecast="2"<option for monthly data>)<br/>

3.If you just want some date's weather prediction with place name: <br/>

from LocationToWeatherAPI import main<br/>
main.driver("Place-Name",date="date string in yyyy-mm-dd format")<br/>

package is installable as "pip install LocationToCliamteAPI"<br/>

If no/wrong keyword arguments given, it may result in wrong output<br/>

Included BROWSABLE API can be started with :<br/>

from LocationToWeatherAPI import api_server<br/>
api_server.start()<br/>

Here the home page, i.e, "/" contains the instructions for accessing the different endpoints.<br/>

For ex:<br/>

"/Name of Place/" or "/Name of Place/1/" - Today's weather for Place<br/>
"/Name of Place/2/" - Monthly forecast for place<br/>
"/Name of Place/3/" - 5 days forecast for place<br/>
"/Name of Place/4/" - 10 days forecast for place<br/>
"/Name of Place/Date/" - Date's forecast for place<br/>
