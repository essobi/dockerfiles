FROM grafana/grafana:4.0.2  
RUN apt-get update && \  
apt-get install -y --no-install-recommends python python-requests && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY start.py /start.py  
  
ENTRYPOINT ["/start.py"]  

