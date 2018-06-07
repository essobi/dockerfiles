FROM python:3.6-slim  
  
MAINTAINER David Raimosson <david.raimosson@mathem.se>  
  
# Pick up some necessary dependencies and tools  
RUN apt-get update && apt-get install -y \  
binutils \  
curl \  
pkg-config \  
git \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip3 --no-cache-dir install \  
awscli \  
boto3 \  
numpy \  
pandas \  
requests  
  
RUN for f in $(find /usr/local/lib/python3.6/site-packages -name "*.so"); do
strip "$f"; done  

