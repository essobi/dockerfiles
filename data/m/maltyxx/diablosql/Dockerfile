FROM debian:jessie  
  
MAINTAINER Yoann Vanitou <yvanitou@gmail.com>  
  
COPY . /opt/diablosql  
  
# Installation de PHP Cli  
RUN apt-get update \  
&& apt-get --yes install php5-cli \  
&& apt-get --yes install php5-mysqlnd \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
  
# Installation de mysql-client  
RUN apt-get update \  
&& apt-get install --yes mysql-client \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
  
VOLUME ["/opt/diablosql/bin", "/opt/diablosql/etc", "/opt/diablosql/sql",
"/opt/diablosql/log"]  
  
WORKDIR "/opt/diablosql"  
  
CMD ["tail", "-f", "/dev/null"]

