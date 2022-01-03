## SUV-s-for-Sale
### Project Overview
The SUVs for Sale project analyses 1000+ SUVs for sale from the Sydney metropolitan area. 

### About The Data
From the listings on the CarSales website, I extracted the following information about each vehicle:
* Title
* Price
* Odometer
* Transmission
* Engine

### Steps Taken
1. Scraped the listing data from the following [base url](https://www.carsales.com.au/cars/new-south-wales-state/sydney-region/suv-bodystyle/) into a csv file for further analysis. Scrapy script used to extract data can be found in the [Sydney_SUV_Scraping folder](https://github.com/jacobpalinski/SUV-s-for-Sale/tree/master/Sydney_SUV_Scraping).
2. Cleaned Data: Extracted year, model and brand from title, replaced null values, and reformatted values.
3. Exploratory Data Analysis

### Analysis of Results
Key findings from analysis:
* SUV prices had a right-tailed distribution with a mean price of $54335.
* Most common brands for sale were Toyota, Audi, Nissan, BMW, and Mazda.
* On average, vehicles had an odometer reading of 56000, with 75% of all vehicles having a reading less than 80,000 km.
* Odometer reading only had a negative correlation of -0.326029 with price. 
* Out of the most affordable brands (mean price within lower quartile), Hyundai depreciated the most.
* Out of the least affordable brands (mean price within upper quartile), Mercedes Benz depreciated the most, depreciating almost 80% in value over an 8 year period.

### Recommendations 
From my analysis, there are implications for both buyers and sellers. 

For buyers who are looking to buy a used car, a Nissan model SUV would be most optimal as it doesn't depreicate greatly both over the short term (<5 years) and long term (>5 years).

Sellers shoud be mindful of the odometer reading of a vehicle when reselling a vehichle. However, they should not be fixated on odometer readings as there are other important factors at play such as maintenance costs, year, brand and fuel consumption, and car specific issues. 



