FROM excelmicro/base:v1.3.0  
LABEL author="Elizabeth Harper <eharper@excelmicro.com>"\  
go-version="1.8.3"\  
description="Golang Environment setup for Excel Micro projects."  
  
RUN apt-get update \  
&& apt-get --yes install git \  
&& wget -q https://storage.googleapis.com/golang/go1.8.3.linux-amd64.tar.gz \  
&& tar -C /usr/local -xzf go1.8.3.linux-amd64.tar.gz \  
&& mkdir /staging  
  
ENV PATH="export PATH=${PATH}:/usr/local/go/bin" \  
GOPATH="/staging"  
ONBUILD RUN ln -s /app /staging/src \  
&& cd /staging/src  
  

