FROM phusion/baseimage:0.9.15  
MAINTAINER scottcase <scott.case.1@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
#Install or Update flexget to v1.2.452 and install latest deluge  
RUN add-apt-repository ppa:deluge-team/ppa  
ADD sources.list /etc/apt/  
RUN apt-get update -q && apt-get install -q -y python-pip deluged deluge-web
python-dev libpcre3-dev  
RUN pip install --upgrade six>=1.70 && pip install flexget && pip install
transmissionrpc  
RUN apt-get clean && rm -rf /tmp/* /var/tmp/* && rm -rf /var/lib/apt/lists/*  
  
#Install init script for flexget  
RUN mkdir /etc/service/flexget  
ADD flexget.sh /etc/service/flexget/run  
RUN chmod +x /etc/service/flexget/run  
  
#Export volumes directory  
VOLUME /config/flexget  
  
#Run my_init  
CMD ["/sbin/my_init"]

