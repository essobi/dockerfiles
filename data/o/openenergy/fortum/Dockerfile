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
ADD src /opt/fortum  
  
# We add the default config parameters to display the available options  
ENV POLL_HOUR 9  
ENV POLL_MINUTE 0  
ENV DATABASE_NAME SURE  
ENV FORTUM_USER user  
ENV FORTUM_PASSWORD password  
ENV INFLUX_HOST 192.168.99.100  
ENV INFLUX_PORT 8086  
ENV INFLUX_USER user  
ENV INFLUX_PASSWORD password  
ENV DATA_SERIES 11996,15953,11995  
ENV VERBOSE False  
ENV STARTUP_TIMEOUT 5  
# Go go go!  
CMD ["python","-u","/opt/fortum/Poll.py"]  

