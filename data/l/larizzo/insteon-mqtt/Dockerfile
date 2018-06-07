FROM python:3.6  
VOLUME /config  
  
RUN apt-get update && \  
apt-get install -y \  
python3-dev \  
python3-pip \  
git && \  
apt-get clean  
  
RUN git clone 'https://github.com/TD22057/insteon-mqtt.git' /opt/insteon-mqtt  
  
RUN pip install /opt/insteon-mqtt  
  
COPY entrypoint.sh entrypoint.sh  
  
CMD ["./entrypoint.sh" ]  

