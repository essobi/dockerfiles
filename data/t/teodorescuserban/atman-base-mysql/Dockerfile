FROM teodorescuserban/atman-base:latest  
  
MAINTAINER Serban Teodorescu, teodorescu.serban@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq -y update && \  
apt-get install -qq -y \  
mysql-server-5.5 \  
mysql-client-5.5 && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /etc/service/mysql  
ADD run /etc/service/mysql/run  
RUN chmod +x /etc/service/mysql/run  
  
RUN sed -i 's/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/'
/etc/mysql/my.cnf && \  
sed -i 's/^key_buffer\s*=/key_buffer_size =/' /etc/mysql/my.cnf  
  
EXPOSE 3306  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
CMD ["/sbin/my_init"]  

