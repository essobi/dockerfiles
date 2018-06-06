FROM ubuntu:12.04  
# basic setup  
RUN cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime  
  
RUN apt-get -yq update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -yq install curl bzip2  
  
# php v5.4  
RUN echo "deb http://ppa.launchpad.net/ondrej/php5-oldstable/ubuntu precise
main " > /etc/apt/sources.list.d/ondrej.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E5267A6C  
RUN apt-get -yq update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -yq install php5-cli php5-curl
php5-gd php5-mysql php5-json php5-mcrypt php5-intl php5-xcache  
  
RUN php5enmod mcrypt  
  
# composer  
RUN DEBIAN_FRONTEND=noninteractive apt-get -yq install git-core  
  
RUN mkdir /user && chown 1000:1000 /user; \  
for ID in 1000 1001 1002 1003; do \  
addgroup --force-badname --gid=$ID $ID; \  
adduser --force-badname --uid=$ID \--gid=$ID \--shell=/bin/bash --home=/user
--no-create-home --gecos "" \--disabled-password $ID; \  
done  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
# finish  
RUN apt-get clean all && rm -rf /var/lib/apt/lists/*  

