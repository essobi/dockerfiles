FROM debian:jessie  
  
LABEL authors="Giovanni Angoli <juzam76@gmail.com>"  
  
COPY entrypoint.sh /  
  
RUN apt-get update && apt-get install -y gcc python-dev python-pip curl
libssl1.0.0 && \  
chmod 755 /entrypoint.sh && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
pip install tornado pycrypto tornado-cors requests  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 8080 8000  

