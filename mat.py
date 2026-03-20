import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))


plt.subplot(2,2,1)
Months = ['Jan','Feb','Mar','Apr','May','Jun']
Sales_A = [200, 250, 300, 280, 350, 400]
Sales_B = [180, 220, 260, 300, 330, 370]
plt.plot(Months,Sales_A,marker='o',color='r',linestyle="dotted",label="Sales_A")
plt.plot(Months,Sales_B,marker='s',color='k',linestyle="dashed",label="Sales_B")
plt.xlabel("Sales")
plt.ylabel("Months")
plt.title("Time_based data")



plt.subplot(2,2,2)
Ad_Spend = [10, 20, 30, 40, 50, 60]
Sales_Scatter = [100, 150, 200, 260, 300, 360]
plt.scatter(Ad_Spend,Sales_Scatter,marker='o',color='k',linestyle='dashed',label="sales")
plt.legend()
plt.xlabel("Ad_Spend")
plt.ylabel("Sales")
plt.title("Ad_Spend vs Sales")


plt.subplot(2,2,3)
Categories = ['Electronics','Clothing','Food','Furniture']
Revenue = [500, 300, 400, 350]
plt.bar(Categories,Revenue,color='r',width=0.5,label='barchart')
plt.legend()
plt.xlabel("Categories")
plt.ylabel("Revenue")
plt.title("Revenue by Category")


plt.subplot(2,2,4)
Regions = ['North','South','East','West']
Region_Sales = [30, 25, 20, 25]

plt.pie(Region_Sales,labels=Regions,autopct='%1.1f%%',startangle=90,explode=[0.1,0,0,0.1])
plt.title("Regional Sales Distribution")
plt.suptitle("sales performance dashboard")
plt.show()