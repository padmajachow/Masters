library("tidyverse")
library("ggplot2")
library("readxl")

# Reading Sales Order data from the Sales Order Excel Sheet
US_Regional_Sales_Data <- read_excel("C:/Users/gorij1p/Downloads/US_Regional_Sales_Data.xlsx", 
                                     sheet = "Sales Orders Sheet")


# Reading Customer data from the Customers Excel Sheet
us_customer_details <- read_excel("C:/Users/gorij1p/Downloads/US_Regional_Sales_Data.xlsx", 
                                  sheet = "Customers Sheet")

# Reading Store Locations data from Store Locations Sheet
us_store_details <- read_excel("C:/Users/gorij1p/Downloads/US_Regional_Sales_Data.xlsx", 
                               sheet = "Store Locations Sheet")

# Joining Sales Order Data and the customer 
# data with the CustomerID column
us_regional_customer_sales_data <- inner_join(US_Regional_Sales_Data,us_customer_details,by="_CustomerID")


# Joining  combined Sales Order Data and the customer 
# data with the store details based on StoreID column
us_regional_customer_store_sales_data <- inner_join(us_regional_customer_sales_data,us_store_details,
                                                    by="_StoreID")

# Save the Final data in the R data format, 
# so that it can be read later for further use.
saveRDS(us_regional_customer_store_sales_data,file = "C:\\Users\\gorij1p\\Downloads\\data\\final_data.rdata")

# Write the final data back to a CSV file.
write.csv(us_regional_customer_store_sales_data,file = "C:\\Users\\gorij1p\\Downloads\\data\\cleaneddata.csv",row.names = FALSE)

# Summary about the data
summary(us_regional_customer_store_sales_data)

# Prints the structure of the data
str(us_regional_customer_store_sales_data)

# Removing the NA rows in the data
us_regional_customer_store_sales_data <- na.omit(us_regional_customer_store_sales_data)

# Replacing the column name with space to underscore("_")

colnames(us_regional_customer_store_sales_data) <- sub(" ", "_", colnames(us_regional_customer_store_sales_data))

# Converting the string data format to the Date data format for the Order Date field
us_regional_customer_store_sales_data$OrderDate <- as.Date(us_regional_customer_store_sales_data$OrderDate)

# Converting the string data format to the Date data format for the Procured Date field
us_regional_customer_store_sales_data$ProcuredDate <- as.Date(us_regional_customer_store_sales_data$ProcuredDate)

# Splitting up the month from the order and storing it in the month column
us_regional_customer_store_sales_data$Month <- format(us_regional_customer_store_sales_data$OrderDate, "%m")

# Calculating the overall price based on quantity, unit price and discount
us_regional_customer_store_sales_data$overall_price <- (us_regional_customer_store_sales_data$Order_Quantity * 
                                                          (us_regional_customer_store_sales_data$Unit_Price - us_regional_customer_store_sales_data$Discount_Applied))

# Barchart for Sales Distribution Channel and No. of Order
ggplot(us_regional_customer_store_sales_data, aes(x = Sales_Channel)) + 
  geom_bar(fill = "coral", color = "black") +
  theme_minimal() +
  labs(title = "Sales Distribution Across Different Channels", x = "Sales Channel", y = "No. of Orders")

# Histogram for an Order Quantity
ggplot(us_regional_customer_store_sales_data, aes(x = Order_Quantity)) + 
  geom_histogram(binwidth = 1, fill = "blue", color = "black") +
  theme_minimal() +
  labs(title = "Histogram of Order Quantities", x = "Order Quantity", y = "Frequency")


# Boxplot for Sales channel and overall price
ggplot(us_regional_customer_store_sales_data, aes(x = Sales_Channel, y = overall_price)) +
  geom_boxplot(fill = "green") +
  theme_minimal() +
  labs(title = "Sales Amount by Region", x = "Sales Channel", y = "Sales Amount")

# Scatter Plot for Unit Price and Unit Cost
ggplot(us_regional_customer_store_sales_data, aes(x = Unit_Cost, y = Unit_Price)) +
  geom_point(color = "red") +
  theme_minimal() +
  labs(title = "Unit Cost vs Unit Price", x = "Unit Cost", y = "Unit Price")




# Linear model to predict the unit price 
# based on the unit cost 
model <- lm(`Unit_Price` ~  `Unit_Cost`, data = us_regional_customer_store_sales_data)

# Print the summary about the model
summary(model)

# Defines a new data frame with the unit cost
new_data <- data.frame(
  `Unit_Cost` = c(3)  
)

# Prediciting the unit price based on the unit cost
predictions <- predict(model, newdata = new_data)

# Print the value
print(predictions)


