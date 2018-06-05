# Use ubuntu 16 based java 8 image  
FROM cogniteev/oracle-java:java8  
MAINTAINER bishesh16  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update apt-get  
RUN apt-get -qq update  
RUN apt-get -qq -y install curl wget unzip  
  
# install mysql with root/root  
RUN echo "mysql-server-5.7 mysql-server/root_password password root" |
debconf-set-selections  
RUN echo "mysql-server-5.7 mysql-server/root_password_again password root" |
debconf-set-selections  
RUN apt-get -y install mysql-server-5.7  
  
RUN mkdir /app  
WORKDIR /app  
  
CMD /bin/bash  

