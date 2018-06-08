#########################################################################################  
# Dockerfile used to automatically build the movierater-machinelearning
microservice  
# Based on ubuntu 14.04.4  
#########################################################################################  
  
# Set the base image as ubuntu 14.04.4  
FROM ubuntu:14.04.4  
  
# Add the current folder  
ADD . /movierater-machinelearning  
  
# Update the apt repository and install some required packages  
RUN apt-get update && apt-get install -y python python-pip python-numpy
python-scipy python-matplotlib ipython ipython-notebook python-pandas python-
sympy python-nose nano  
  
# Install required python packages  
RUN pip install Flask scikit-learn sklearn  
  
# Expose port 5000  
EXPOSE 5000  
  
# Start the api  
CMD ["python", "/movierater-machinelearning/api/app.py"]

