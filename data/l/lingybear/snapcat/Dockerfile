# Use an official Python runtime as a parent image  
FROM python:3.6-slim  
  
# matplotlib config  
RUN mkdir -p /root/.config/matplotlib  
RUN echo "backend : Agg" > /root/.config/matplotlib/matplotlibrc  
  
# Set the working directory to /snapcat  
WORKDIR /snapcat  
  
# Install any needed packages specified in requirements.txt  
COPY requirements.txt /snapcat  
RUN pip install -r requirements.txt  
  
# Copy the current directory contents into the container at /app  
ADD . /snapcat  
  
# Make port 80 available to the world outside this container  
EXPOSE 80  
# Run server.py when the container launches  
CMD ["python", "server.py"]  

