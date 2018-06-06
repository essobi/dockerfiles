FROM ubuntu:15.04  
MAINTAINER Dan Wanek <dan@crisply.com>  
LABEL Description="This image is used to build an RVM system installation."  
VOLUME ["/usr/local/rvm"]  
ENV PATH
/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
USER root  
RUN apt-get update -qq  
RUN apt-get install -y curl git build-essential libpq-dev libyaml-dev \  
libcurl4-openssl-dev gawk libreadline6-dev libsqlite3-dev sqlite3 autoconf \  
libgdbm-dev libncurses5-dev automake libtool bison pkg-config libffi-dev \  
sudo  
RUN apt-get clean  
RUN groupadd -r rvm -g 1000 && \  
useradd -u 1000 -r -g rvm -d /home/rvmuser -m -s /bin/bash -c "RVM Image User"
rvmuser  
COPY install/run-rvm.sh /usr/local/bin/  
RUN chmod 0755 /usr/local/bin/run-rvm.sh  
ENTRYPOINT ["/usr/local/bin/run-rvm.sh"]  

