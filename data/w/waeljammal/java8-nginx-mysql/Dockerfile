FROM ubuntu:14.04  
MAINTAINER Wael Jammal  
  
### BASIC CONFIG  
RUN mkdir -p /mnt/logs  
RUN chmod 777 /mnt/logs  
RUN apt-get -q update  
RUN apt-get install -q -y software-properties-common wget curl git nano  
  
# NODEJS  
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
  
# JAVA8  
RUN /usr/bin/add-apt-repository ppa:webupd8team/java 2> /dev/null  
  
# MISC  
RUN apt-get -qq update  
RUN mkdir -p /home/root/backuper/  
RUN mkdir -p /tmp/  
RUN /bin/echo oracle-java8-installer shared/accepted-oracle-license-v1-1
select true | sudo /usr/bin/debconf-set-selections  
  
### TIMEZONE  
RUN echo "America/Sao_Paulo\n" > '/etc/timezone'  
RUN /usr/sbin/dpkg-reconfigure --frontend noninteractive tzdata 2> /dev/null  
  
### less frequent version changes  
RUN apt-get install -qq -y tar unzip zip python-dateutil ant nginx git  
  
# more frequent version changes  
RUN apt-get install -qq -y oracle-java8-installer mysql-client nodejs  
  
### NEWRELIC Server Monitoring  
RUN echo "deb http://apt.newrelic.com/debian/ newrelic non-free" >>
/etc/apt/sources.list.d/newrelic.list  
RUN /usr/bin/wget -q -O- https://download.newrelic.com/548C16BF.gpg | apt-key
add -  
RUN apt-get -qq update  
  
### MYSQL (optional startup)  
RUN sudo apt-get install -qq -y mysql-server 2> /dev/null  
  
### NGINX redir to tomcat  
COPY config/nginx.conf /etc/nginx/nginx.conf  
  
CMD ["bash"]

