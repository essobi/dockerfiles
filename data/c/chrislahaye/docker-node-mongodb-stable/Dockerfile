FROM node:9.8.0  
RUN apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 \--recv EA312927 \  
&& echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.4 main" |
tee /etc/apt/sources.list.d/mongodb-org-3.4.list \  
&& apt-get update \  
&& apt-get install -y \--force-yes mongodb-org \--no-install-recommends \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

