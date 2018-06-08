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
ADD src /opt/ic  
  
# We add the default config parameters to display the available options  
ENV POLL_INTERVAL 15  
ENV DATABASE_NAME SURE  
ENV IC_USER user  
ENV IC_PASSWORD password  
ENV INFLUX_HOST 192.168.99.100  
ENV INFLUX_PORT 8086  
ENV INFLUX_USER root  
ENV INFLUX_PASSWORD root  
ENV VERBOSE False  
ENV REQUEST_TIMEOUT 5000  
ENV STARTUP_TIMEOUT 5  
# Go go go!  
CMD ["python","-u","/opt/ic/Poll.py"]  

