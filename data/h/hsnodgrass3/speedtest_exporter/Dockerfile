FROM python:3.6  
LABEL maintainer="heston.snodgrass@connexta.com" \  
version="1.0"  
RUN mkdir /opt/speedtest_exporter  
  
ADD speedtest_exporter.py /opt/speedtest_exporter  
  
RUN pip3 install speedtest-cli prometheus_client  
  
ENTRYPOINT exec python3 /opt/speedtest_exporter/speedtest_exporter.py

