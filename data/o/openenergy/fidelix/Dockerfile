# This indicates what base image you are using and who maintains the
Dockerfile.  
FROM python:2  
MAINTAINER Leo Fidjeland (hello@leo.wtf)  
  
# Upgrade pip  
RUN pip install --upgrade pip  
  
# We add requirements first so that we don't have to rebuild everytime we
change the source  
ADD requirements.txt /opt  
RUN pip install -r /opt/requirements.txt  
  
# Add the source  
ADD src /opt/fidelix  
  
# We add the default config parameters to display the available options  
ENV POLL_INTERVAL 5  
ENV FIDELIX_USER user  
ENV FIDELIX_PASSWORD pass  
ENV MQTT 192.168.99.100  
ENV VERBOSE False  
ENV REQUEST_TIMEOUT 5000  
# Go go go!  
CMD ["python","-u","/opt/fidelix/Poll.py"]  

