FROM rocker/rstudio:latest  
  
MAINTAINER "Sean Abbott" sabbott@finmason.com  
  
  
RUN apt-get update && apt-get install -y \  
libnss-sss \  
libpam-sss \  
libpq-dev \  
openssh-client \  
python-dev \  
python-pip \  
sssd \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY sss_client.pam /etc/pam.d/sss_client  
COPY get-pip.py /tmp/  
  
COPY requirements.txt /tmp/  
# I don't like having a binary like get-pip in here, but I like  
# the idea of wgetting the script less...  
# https://bootstrap.pypa.io/get-pip.py  
RUN python /tmp/get-pip.py \  
&& pip install --upgrade pip \  
&& pip install --requirement /tmp/requirements.txt  
  
COPY Docker_Package_Installation.R /tmp/  
RUN /tmp/Docker_Package_Installation.R  

