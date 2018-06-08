FROM sameersbn/ubuntu:14.04.20151213  
MAINTAINER sameer@damagehead.com  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv C7917B12 \  
&& echo "deb http://ppa.launchpad.net/chris-lea/node.js/ubuntu trusty main" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs \  
&& adduser --disabled-login --gecos 'NodeJS' nodejs \  
&& npm install -g express-generator nodemon \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY scripts /scripts  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
ENTRYPOINT ["/sbin/entrypoint.sh"]  

