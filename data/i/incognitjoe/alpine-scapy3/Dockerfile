FROM alpine  
  
RUN apk add --update python3 && \  
python3 -m pip install scapy-python3 && \  
mkdir -p /opt/data/  
WORKDIR /opt/data  
ENTRYPOINT ["python3"]  

