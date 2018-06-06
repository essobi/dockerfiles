  
# Use java as parent image  
FROM java:latest  
  
# Set the working directory to /app  
WORKDIR /app  
  
# Copy the app/chart directory contents into the container at /app  
ADD . /app  
  
# Copy the local repository into container  
# ADD ~/.m2 ~/.m2  
# Make port 80 available to the world outside this container  
EXPOSE 8080  
# Define enviroment variable  
ENV JAVA_HOME /opt/java  
ENV NAME work  
  
# Run command when the container launches  
# CMD ["java", "-jar", "chart-0.0.1-SNAPSHOT.jar"]  

