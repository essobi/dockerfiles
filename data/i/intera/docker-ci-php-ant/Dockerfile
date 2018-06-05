FROM intera/docker-ci-php:5.6-ubuntu  
  
RUN apt-get update \  
&& apt-get dist-upgrade -y \  
&& apt-get install -y \  
gettext \  
curl \  
default-jdk \  
ant \  
ruby-compass \  
mysql-client \  
  
&& apt-get \--purge autoremove \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

