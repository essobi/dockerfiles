FROM ubuntu:16.04  
ENV COINBASE_API_KEY SECRET  
ENV COINBASE_API_SECRET_KEY SECRET  
ENV INFLUXDB_HOST localhost  
RUN apt -y update && \  
apt -y install python3 python3-pip && \  
pip3 install --upgrade pip  
COPY . /opt/  
WORKDIR /opt  
RUN pip3 install -r requirements.txt  
CMD python3 coinbase_to_influxdb.py  

