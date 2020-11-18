# sqlalchemy_challenge

## Climate Analysis and Exploration
### Precipitation Analysis

- Query the last 12 months of precipitation data, and plot the results using the DataFrame plot method.

Precipitation Plot

![precipiation](https://user-images.githubusercontent.com/69160361/99486651-d3dbf780-2921-11eb-9ba7-3994c1ea703f.png)

- Display the summary statistics for the precipitation data.

<img width="154" alt="Screen Shot 2020-11-18 at 2 50 27 PM" src="https://user-images.githubusercontent.com/69160361/99592473-82794a00-29ad-11eb-827b-81bf5d84e139.png">

### Station Analysis

- Design a query to find the most active station.
- Calculate the lowest temperature recorded, the highest temperature recorded, and the average temperature of the most active station.

<img width="1003" alt="Screen Shot 2020-11-18 at 2 26 03 PM" src="https://user-images.githubusercontent.com/69160361/99590027-09c4be80-29aa-11eb-828d-8aad6f8c60b2.png">

- Query the last 12 months of temperature data (TOBS) for the most active station (USC00519281) and plot the results as a histogram.

Histogram: Station USC00519281 temperature observation data (TOBS) over 12 months 

![Histogram](https://user-images.githubusercontent.com/69160361/99486930-6e3c3b00-2922-11eb-86a5-d987359a876b.png)

## Climate App

After completing my first analyses, I designed a Flask API based on the queries I developed.

Available Routes:

Home Page

<img width="181" alt="Screen Shot 2020-11-18 at 2 41 34 PM" src="https://user-images.githubusercontent.com/69160361/99591733-78a31700-29ac-11eb-9381-3487960814b0.png">

Precipitation

<img width="391" alt="Screen Shot 2020-11-18 at 2 41 55 PM" src="https://user-images.githubusercontent.com/69160361/99591767-85c00600-29ac-11eb-8123-8b6e3d0c4b1d.png">

Stations

<img width="379" alt="Screen Shot 2020-11-18 at 2 42 08 PM" src="https://user-images.githubusercontent.com/69160361/99591811-91abc800-29ac-11eb-886f-413287f8e942.png">

TOBS

<img width="358" alt="Screen Shot 2020-11-18 at 2 42 20 PM" src="https://user-images.githubusercontent.com/69160361/99591849-9d978a00-29ac-11eb-88f0-ab1ffe683293.png">

/api/v1.0/<start>

<img width="409" alt="Screen Shot 2020-11-18 at 2 42 44 PM" src="https://user-images.githubusercontent.com/69160361/99591931-b738d180-29ac-11eb-95d7-31a917545d49.png">

/api/v1.0/<start>/<end>

<img width="489" alt="Screen Shot 2020-11-18 at 2 43 17 PM" src="https://user-images.githubusercontent.com/69160361/99591957-c029a300-29ac-11eb-9c9e-76a3593552e0.png">

## Bonus Section
### Temperature Analysis 1

For identifying the difference in means for average June temperature and average December temperature, we will use a paired t-test because we are measuring the same sample (temperatures at the 9 different Hawaii stations) under different conditions (June vs. December). We are comparing the means from the same group(s) (the 9 stations) at different times (two different months). 

The result of this t-test was a p value of p < .001, which shows that there is a strong, statistically significant difference between the average temperatures in June and the average temperatures in December for all of the stations.

<img width="632" alt="Screen Shot 2020-11-18 at 2 21 11 PM" src="https://user-images.githubusercontent.com/69160361/99589589-6e334e00-29a9-11eb-8d3d-7783b72ba775.png">

### Temperature Analysis 2

I selected 04/20/2016 as my trip date, and used the function 'calc_temps' to calculate the min, avg, and max temperatures for my trip using the matching date from the previous year (04/20/2015).
To plot the results of my query as a bar chart, I used average temperature for the y-value, and used the peak-to-peak (max temp- min temp) value as my y error bar.

Trip Average Temperature Bar Chart

![TripAvgTemp](https://user-images.githubusercontent.com/69160361/99486707-f53ce380-2921-11eb-85b5-6212c1a0b3fc.png)

### Daily Rainfall Average

After querying the total amount of rainfall per wather station for my trip dates (using the previous year matching date), I used the function 'daily_normals' to calculate the daily normals for my trip (trip dates 04/10/2016 - 04/20/2016). This function returned the minimum temperature, maximum temperature, and average temperature for each date of my trip. After storing the results in a DataFrame, I plotted the daily normals as an area plot.

Daily Normals DataFrame

<img width="249" alt="Screen Shot 2020-11-18 at 2 38 26 PM" src="https://user-images.githubusercontent.com/69160361/99591373-ed298600-29ab-11eb-9a01-ee756bc52fa5.png">

Daily Normals Area Plot

![DailyNormals](https://user-images.githubusercontent.com/69160361/99486630-ca528f80-2921-11eb-8d98-0bfcd63f42b4.png)
