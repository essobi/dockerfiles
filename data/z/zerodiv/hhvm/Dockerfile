##  
# We start from the basic hhvm image.  
##  
FROM hhvm/hhvm:3.18-lts-latest  
  
# setup the root home  
ENV HOME /root  
  
# Turn off apt-get being prompty  
ENV DEBIAN_FRONTEND noninteractive  
  
# bring all updates in  
RUN apt-get update -y  
  
# install the mysql server  
RUN apt-get install -y mysql-server  
  
# install postgresql  
RUN apt-get install -y postgresql postgresql-contrib  
  
# install the composer binary to /usr/local/bin  
RUN curl https://getcomposer.org/installer | hhvm --php -- /dev/stdin
--install-dir=/usr/local/bin --filename=composer  

