FROM ubuntu-debootstrap:trusty  
MAINTAINER https://m-ko-x.de Markus Kosmal <code@m-ko-x.de>  
  
RUN apt-get update -yqq && \  
apt-get install --no-install-recommends -yqq \  
curl \  
nano \  
python \  
build-essential \  
git \  
ca-certificates  
  
ADD ./nodejs/* /nodejs/  
  
RUN ls -hAlf / && ls /nodejs  
  
ENV PATH $PATH:/nodejs/bin

