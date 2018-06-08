# Use an official Python runtime as a parent image  
FROM python:2.7  
# Set add the 'en_US.utf8' locale to the image  
ARG DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && \  
apt-get install -y apt-utils locales && \  
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \  
locale-gen  
  
# Set the working directory to /code  
WORKDIR /code  
  
# Create the django user and take ownership of /code  
RUN adduser --no-create-home --disabled-login --group --system django && \  
chown -R django:django /code  
  
# Copy the pip requirementes file to /code  
COPY requirements.txt /code  
  
# Install any needed packages specified in requirements.txt  
RUN pip install -r requirements.txt  
  
# Execute start script  
CMD ["/bin/bash", "-c", "python"]  
  

