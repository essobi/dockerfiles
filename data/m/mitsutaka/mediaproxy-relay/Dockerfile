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
apt-get install -y mediaproxy-relay  
  
RUN apt-get purge -y ca-certificates libidn11 openssl wget  
  
COPY entrypoint.sh /  
RUN chown root.root /entrypoint.sh && chmod 700 /entrypoint.sh  
  
EXPOSE 20000-60000/udp  
  
ENTRYPOINT ["/entrypoint.sh"]  

