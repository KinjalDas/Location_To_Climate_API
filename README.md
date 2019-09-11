# Location_To_Climate_API

This API is used for converting location name as a string to the respective locality's weather data. Import "main.driver(place,date="<date in string format>",type_of_forecast="<Any one from 1 to 4 in string format>") from package "LocationToCliamteAPI". You can pass ANY ONE OF the keyword arguments - Date in "YYYY-MM-DD" format/ forecast type required ('1' for today {Default Selection}, '2' for monthly,'3' for 5-day and '4' for 10-day). We are relying on APIs used by weather.com internally for extracting the respective data.

For ex:

If you just want today's weather metrics with place name: LocationToCliamteAPI.main.driver("Place-Name")

If you just want the current month's with place name: LocationToCliamteAPI.main.driver("Place-Name",type_of_forecast="2"<option for monthly data>)

If you just want some date's weather prediction with place name: LocationToCliamteAPI.main.driver("Place-Name",date="date string in yyyy-mm-dd format")

package is installable as "pip install LocationToCliamteAPI"

If no/wrong keyword arguments given, it may result in wrong output
