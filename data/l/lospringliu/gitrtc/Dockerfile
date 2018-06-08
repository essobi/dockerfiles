FROM ibmjava:latest  
  
MAINTAINER Xinchun Liu <lospringliu@gmail.com>  
  
RUN ln -sf /usr/share/zoneinfo/America/Toronto /etc/localtime && dpkg-
reconfigure -f noninteractive tzdata  
  
RUN apt-get update && apt-get install -y unzip telnet iputils-ping net-tools
vim python3-pip libmysqlclient-dev git && pip3 install --upgrade pip && pip3
install django docutils mysqlclient django-mptt django-reversion  
  
RUN locale-gen "en_US.UTF-8"  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN mkdir -p /root/bin  
COPY .profile /root/  
COPY .bashrc /root/  
COPY .gitconfig /root/  
COPY README /root  
  
RUN mkdir -p /workdir  
  
EXPOSE 8000  

