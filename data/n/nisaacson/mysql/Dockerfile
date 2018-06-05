FROM ubuntu:12.10  
MAINTAINER Noah Isaacson noah@nisaacson.com  
  
# Update the APT cache  
RUN sed -i.bak 's/main$/main universe/' /etc/apt/sources.list  
RUN apt-get update  
  
# Install and setup project dependencies  
RUN apt-get install -y curl lsb-release supervisor openssh-server build-
essential  
RUN apt-get install -qqy python-software-properties  
RUN apt-get install -qqy vim  
  
RUN mkdir -p /var/run/sshd  
RUN mkdir -p /var/log/supervisor  
  
RUN locale-gen en_US en_US.UTF-8  
  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
# RUN ln -s /bin/true /sbin/initctl  
RUN apt-get -y install mysql-client mysql-server  
RUN apt-get -y install pwgen  
  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
  
ADD ./bin /opt/bin  
  
ADD ./etc/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN echo 'root:root' | chpasswd  
  
EXPOSE 3306  
EXPOSE 22  
CMD ["/bin/bash", "/opt/bin/run.sh"]  

