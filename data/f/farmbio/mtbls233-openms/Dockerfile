# swift, openMS, parameters etc. for the MTBLS233-POP project  
FROM ubuntu:14.04  
MAINTAINER Anders Larsson <anders.larsson@icm.uu.se>  
  
# Install OpenMS & Swift -requirements  
RUN apt-get update -y && \  
apt-get upgrade -y && \  
apt-get install -y \  
openms \  
libffi-dev \  
libssl-dev \  
python-dev \  
python-pip  
  
# Install Swift-pythonclient  
RUN pip install \  
pyopenssl \  
ndg-httpsclient \  
pyasn1 \  
python-keystoneclient \  
python-swiftclient  
  
# project parameterfiles  
COPY params_MTBLS233 /params_MTBLS233  
  
# project binary for running openMS on swift files  
COPY bin /bin  
  

