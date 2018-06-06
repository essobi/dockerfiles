# Header  
FROM ubuntu:latest  
  
ENV LATEST_VERSION "1.46"  
# Install dependencies  
RUN apt-get update && apt-get -y install \  
build-essential \  
libdbd-mysql-perl \  
libsparsehash-dev \  
libspreadsheet-writeexcel-perl \  
mysql-client \  
php7.0 \  
php7.0-mysql \  
zlibc \  
zlib1g \  
zlib1g-dev  
  
# Install Stacks -- latest version at time of container creation  
ADD
http://catchenlab.life.illinois.edu/stacks/source/stacks-$LATEST_VERSION.tar.gz
stacks.tar.gz  
RUN mkdir stacks  
RUN tar xfvz stacks.tar.gz -C stacks --strip-components 1  
RUN cd ./stacks && ./configure --enable-sparsehash && make && make install  
  
# Use the default config  
#ADD mysql.cnf /usr/local/share/stacks/sql/mysql.cnf  
# Add config for Apache 2.4+  
#ADD stacks.conf /etc/apache2/conf-available/stacks.conf  
#RUN ln -s /etc/apache2/conf-available/stacks.conf /etc/apache2/conf-
enabled/stacks.conf  

