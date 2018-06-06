FROM ubuntu:latest  
  
RUN apt-get update -qq -y &&\  
apt-get -qq -y install software-properties-common curl &&\  
add-apt-repository -y ppa:devel-k/log-courier &&\  
apt-get update -qq -y &&\  
apt-get -qq -y install log-courier &&\  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["/usr/sbin/log-courier", "-config", "/etc/log-courier/log-courier.conf"]  
  

