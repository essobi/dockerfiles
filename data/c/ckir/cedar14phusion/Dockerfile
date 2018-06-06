FROM heroku/cedar:14  
  
ADD ./phusion /bd_build  
  
RUN echo "Updating " && \  
echo "deb http://archive.ubuntu.com/ubuntu/ trusty main restricted universe
multiverse" > /etc/apt/sources.list && \  
echo "deb-src http://archive.ubuntu.com/ubuntu/ trusty main restricted
universe multiverse" >> /etc/apt/sources.list && \  
echo "deb http://archive.ubuntu.com/ubuntu/ trusty-security main restricted
universe multiverse" >> /etc/apt/sources.list && \  
echo "deb http://archive.ubuntu.com/ubuntu/ trusty-updates main restricted
universe multiverse" >> /etc/apt/sources.list && \  
echo "deb http://archive.ubuntu.com/ubuntu/ trusty-proposed main restricted
universe multiverse" >> /etc/apt/sources.list && \  
echo "deb http://archive.ubuntu.com/ubuntu/ trusty-backports main restricted
universe multiverse" >> /etc/apt/sources.list && \  
echo "deb-src http://archive.ubuntu.com/ubuntu/ trusty-security main
restricted universe multiverse" >> /etc/apt/sources.list && \  
echo "deb-src http://archive.ubuntu.com/ubuntu/ trusty-updates main restricted
universe multiverse" >> /etc/apt/sources.list && \  
echo "deb-src http://archive.ubuntu.com/ubuntu/ trusty-proposed main
restricted universe multiverse" >> /etc/apt/sources.list && \  
echo "deb-src http://archive.ubuntu.com/ubuntu/ trusty-backports main
restricted universe multiverse" >> /etc/apt/sources.list && \  
apt-get update && \  
/bd_build/prepare.sh && \  
/bd_build/system_services.sh && \  
/bd_build/utilities.sh && \  
/bd_build/fix_pam_bug.sh && \  
/bd_build/cleanup.sh \  
  
ENV TZ=UTC  
  
CMD ["/sbin/my_init"]  
  

