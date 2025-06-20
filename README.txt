Python Mortality Rate

1) What our project does

This project is designed to help users understand how personal factors (such as age, gender, and smoking status) affects their risk of mortality and insurance premium rates. By using publicly available mortality tables, the application visualizes there risks and estimates simplifies insurance premiums. Users can input their characteristics to see their positioning on interactive graphs and explore hypothetical scenarios such as the impact of quitting smoking or aging on their insurance rates

Below are some features.

Mortality Rate Vizualization:
Displays mortality rates based on public datasets, allowing users to visualize risks by age, gender, and smoking status
Interactive Risk Analysis:
Users can input their own characteristics to see where they fall on the risk curve and compare different scenarios
Premium Estimator:
Provides a very rough estimate of premium, given age and smoking status. Gender is not included as a factor
Scenario Simulation:
Allows users to experiment with factors like age changes or smoking status to view potential impacts on both premium and mortality rates

2) How to install dependencies

Below is the technology we used.

- Python: Logic and data handling
- Pyplot: Data Visualization
- Pandas: Data Organization
- Tkinter: User Interface

Since Python and Tkinter are already built in, you only need to install pandas and matplotlib for pyplot.

conda install pandas
conda install matplotlib

3) How to run and use your project

You should download these files: data_cleaning.py, graph.py, user_interface.py, and 6 CSV files containing mortality data. The 6 CSV files can be found from this Society of Actuaries website:

https://mort.soa.org/

The left column has the table numbers. You should download tables 3372, 3371, 3370, 3369, 3336, and 3326 as CSV files.

You should put all of these in the same folder. Additionally, you should make a separate subfolder named "unclean_csv" inside the folder and put all 6 CSV files in the subfolder. Then, you should run user_interface.py.

An example usage would be to type "35" in the Age text box, "Male" in the Gender text box, "Y" in the Smoker text box, and click the Compare Gender checkbox. Then, you can click the Display My Mortality button which will open an HTML file with an interactive graph in your browser. The graph has a vertical red line which is to show that there isn't much data to the right of that line and that portion might thus be unreliable. You can also click on the Calculate My Premium button which will provide a rough estimate of a range for your premium.

4) What outputs to expect

A Tkinter GUI will open once you run user_interface.py. From there, there are 3 text boxes to input age, gender, and smoking status. To display mortality, you can either enter valid inputs or leave any of them blank. However, for the premium calculation, you must input both a valid age and smoking status.

5) Any setup instructions or limitations

A limitation is that we assume you are using Anaconda for Python.


Contributers
- Philip Tan
- Oscar Ramirez
