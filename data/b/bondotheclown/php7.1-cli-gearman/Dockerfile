FROM ubuntu:16.04  
  
RUN apt-get update -y  
RUN apt-get install -y python-software-properties software-properties-common
language-pack-en-base  
RUN LC_ALL=en_US.UTF-8 add-apt-repository -y ppa:ondrej/php  
RUN LC_ALL=en_US.UTF-8 add-apt-repository -y ppa:ondrej/pkg-gearman  
RUN apt-get update -y  
  
RUN apt-get install -y php7.1-cli php7.1-gearman php7.1-xml php7.1-mbstring \  
php7.1-xdebug php7.1-curl php7.1-mysql php7.1-sqlite3 \  
php7.1-redis unzip curl  
RUN rm /etc/php/7.1/cli/conf.d/20-xdebug.ini  
  
# Clean up.  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

