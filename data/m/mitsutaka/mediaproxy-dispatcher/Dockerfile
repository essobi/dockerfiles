FROM ubuntu:14.04  
MAINTAINER "Mitz Amano <mitz@linux.com>"  
USER root  
  
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt trusty main restricted
universe multiverse" > /etc/apt/sources.list && \  
echo "deb mirror://mirrors.ubuntu.com/mirrors.txt trusty-updates main
restricted universe multiverse" >> /etc/apt/sources.list && \  
echo "deb mirror://mirrors.ubuntu.com/mirrors.txt trusty-security main
restricted universe multiverse" >> /etc/apt/sources.list  
  
RUN apt-get update && \  
apt-get install -y wget  
  
RUN echo "deb http://ag-projects.com/ubuntu trusty main"
>>/etc/apt/sources.list && \  
wget -O - http://download.ag-projects.com/agp-debian-gpg.key | apt-key add -  
  
RUN apt-get update && \  
apt-get install -y mediaproxy-dispatcher python-mysqldb  
  
RUN mkdir -p /etc/mediaproxy/script  
COPY script/statistic.sql /etc/mediaproxy/script  
  
COPY entrypoint.sh /sbin  
RUN chown root.root /sbin/entrypoint.sh && chmod 700 /sbin/entrypoint.sh  
  
VOLUME ["/run/mediaproxy"]  
VOLUME ["/etc/mediaproxy"]  
EXPOSE 25060/tcp  
  
ENTRYPOINT ["entrypoint.sh"]  

