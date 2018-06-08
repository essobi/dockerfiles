FROM mesosphere/spark:latest  
  
# Install pip package for installation of the nssift binaries.  
RUN apt update && apt install -y python3-pip python3-tk pandoc  
  
# Copy the python package and install it using pip.  
COPY . /tmp/nssift  
RUN pip3 install -U pip wheel  
RUN pip3 install /tmp/nssift  

