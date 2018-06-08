FROM ubuntu:14.04  
# Update packages  
RUN apt-get update -y  
  
# Install Python Setuptools  
RUN apt-get install -y python-setuptools  
  
# Install pip  
RUN easy_install pip  
  
# Add and install Python modules  
ADD requirements.txt /src/requirements.txt  
RUN cd /src; pip install -r requirements.txt  
  
# Bundle app source  
ADD . /src  
RUN mkdir ~/.stormpath/  
COPY docker/stormpath/apiKey.properties ~/.stormpath/  
  
# Expose  
EXPOSE 5000  
# Run  
CMD ["python", "/src/run.py", "--host=0.0.0.0", "--view"]  

