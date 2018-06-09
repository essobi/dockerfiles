FROM phusion/baseimage  
# Ensure UTF-8  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV HOME /root  
CMD ["/sbin/my_init"]  
  
RUN apt-get update && \  
apt-get -y install software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
apt-get update && \  
apt-get -y install oracle-java8-installer supervisor  
  
###### Chaning timezone ######  
RUN set -x && \  
unlink /etc/localtime && \  
ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
COPY supervisord.conf /etc/supervisord.conf  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

