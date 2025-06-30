# CS340
Overview / Motivation:
The Grazioso Salvare animal shelter project is an interactive web application designed to aid in animal rescue efforts by leveraging the Austin Animal Center Outcomes dataset. This dashboard allows users to efficiently filter data related to specific types of rescue operations and visualize the information through interactive elements, including maps, charts, and data tables. The inclusion of a pie chart enhances the dashboard's usability by effectively illustrating the distribution of animal outcomes, providing quick insights into the success rates of various adoption strategies.
Required Functionality:
The dashboard integrates the following essential features:
1. Interactive Filtering Options: Users can filter the dataset based on various rescue operation types:
   - Water Rescue
   - Mountain/Wilderness Rescue
   - Disaster Rescue and Individual Tracking
   - Reset to view the complete dataset

2. Data Table: A dynamic table that displays detailed information about the animals, updating in real-time as filters are applied.

3. Geolocation Map: A map component visualizing the locations where animal rescues occur, assisting in planning and analysis for rescue operations.

4. Bar Chart: A bar chart that provides insights into the quantity of different animal breeds rescued, adapting automatically to the applied filters.

5. Pie Chart: The pie chart visualizes the distribution of animal outcomes (e.g., adopted, returned, etc.), offering a clear and immediate understanding of how many animals succeed in finding homes.

Tools and Technologies:
- MongoDB: Selected for its flexibility and scalability, MongoDB is an ideal NoSQL database for managing unstructured data here. Its document-oriented model easily accommodates the diverse data that comes with animal rescue operations. MongoDB's integration with Python via the Pymongo library streamlines data manipulation and retrieval, facilitating effective operation of the dashboard.

- Dash Framework: Dash allows for the creation of interactive web applications in Python without requiring HTML or JavaScript. Its component-based architecture and callback mechanism serve as the view and control layers, managing user interactions and dynamic updates to content. The selection of Dash reflects its robustness in building data-driven applications and its wide range of support for interactive components, making it particularly fitting for the Grazioso Salvare Dashboard.

Project Reproduction Steps:
1. Setup MongoDB: Install MongoDB and import the Austin Animal Center Outcomes dataset into a designated collection.

2. Install Dependencies: Use `pip` to install the required Python libraries:
   ```bash
   pip install dash pandas plotly pymongo dash-leaflet
   ```

3. Run the Dashboard: Execute the Python script containing the dashboard code, ensuring MongoDB is operational and accessible.

4. Access the Dashboard: Open a web browser and navigate to the URL outputted by the dashboard code.

Challenges:
One significant challenge faced during development was ensuring that the filters, pie chart, bar chart, and map components correctly synchronized in response to user interactions. This was effectively addressed by utilizing Dash's callback system, which allowed for the dynamic updating of visual and tabular components based on user selections. This approach not only resolved the interactivity issues but also ensured a seamless user experience across all dashboard elements.








Screenshots:
 
 
 
 
 
