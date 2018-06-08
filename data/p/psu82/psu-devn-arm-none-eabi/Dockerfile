# Use an official Ubuntu latest long term support version as a base image  
FROM ubuntu:latest  
  
# Set the working directory to /opt/psu-devn-monit  
WORKDIR /opt/psu-devn-monit  
  
# Copy the current directory contents into the container at /opt/psu-devn-
monit  
ADD . /opt/psu-devn-monit  
  
# Install all needed packages  
RUN apt-get update && apt-get install -y \  
python \  
python-pip \  
make \  
cmake \  
gcc-arm-none-eabi \  
gdb-arm-none-eabi \  
qemu  
  
# Install any needed python packages specified in requirements.txt  
#RUN pip install -r requirements.txt  
# Make port 80 available to the world outside this container  
#EXPOSE 80  
# Run monit.py when the container launches  
#CMD ["python", "/opt/psu-devn-monit/monit.py"]  

