FROM python:2.7  
LABEL maintainer="allxone@hotmail.com"  
  
# Copy over and install the requirements  
COPY ./requirements.txt /requirements.txt  
COPY ./mqtt-tfserving.py /mqtt-tfserving.py  
COPY ./utils /utils  
  
RUN pip install -r /requirements.txt  
  
ENV SCORING_ADDRESS localhost:9000  
ENV MQTT_SERVER 127.0.0.1  
ENV MQTT_SERVER_PORT 1883  
ENV MODEL_NAME model  
ENV MODEL_VERSION 1  
ENV TFS_TIMEOUT 60  
ENV TFS_THRESHOLD 0.5  
CMD [ "python", "/mqtt-tfserving.py" ]  
  
# EXAMPLE USAGE:  
# docker run --rm -e SCORING_ADDRESS=35.184.216.154:80 -e
MQTT_SERVER=35.224.247.149 -it allxone/tensorplate:mqtt-tfserving /bin/bas  

