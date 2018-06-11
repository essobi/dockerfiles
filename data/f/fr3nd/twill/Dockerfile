FROM debian:jessie  
MAINTAINER Carles Amigó, fr3nd@fr3nd.net  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
libxml2-dev \  
libxslt1-dev \  
python-dev \  
python-pip \  
zlib1g-dev \  
&& rm -rf /usr/share/doc/* && \  
rm -rf /usr/share/info/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/*  
  
ENV TWILL_VERSION=1.8.0  
ENV PYTEST_VERSION=2.9.1  
  
RUN pip install \  
requests==2.10.0 \  
cssselect==0.9.1 \  
lxml==3.6.0 \  
twill==$TWILL_VERSION \  
pytest==$PYTEST_VERSION \  

