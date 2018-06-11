# DOCKER-VERSION 1.0.0  
FROM ubuntu:14.04  
MAINTAINER Rob Landers <landers.robert@gmail.com>  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y wget build-essential software-properties-common curl rsync
dnsutils unzip inotify-tools python python-pip && \  
apt-get purge -y python-pip python-requests && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
curl -sSLO https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py && \  
pip install consulate && \  
pip install \--upgrade requests  
  
ENV PATH /package/admin/s6-2.1.3.0/command:$PATH  
ENV GOMAXPROCS 100  
  
RUN touch /etc/leapsecs.dat  
  
ADD root /  
  
ENTRYPOINT ["/package/admin/s6-2.1.3.0/command/s6-svscan","/etc/s6"]  
CMD []

