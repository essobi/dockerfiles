FROM python:3.5  
  
RUN apt-get update && \  
apt-get -y install build-essential \  
python3-dev \  
libffi-dev \  
libssl-dev  
  
RUN pip3 install jira==1.0.3 \  
cryptography \  
PyJWT \  
IPython==4.0.0  
  
ENTRYPOINT ["/usr/local/bin/jirashell"]  

