FROM netpositivehu/dotdeb-php7.0-qatools  
  
MAINTAINER info@netpositive.hu  
  
RUN apt-get update -y  
  
# mysql-client  
RUN apt-get install -y mysql-client  
  
# Sitebuild related packages  
RUN apt-get install -y \  
nodejs \  
nodejs-legacy \  
npm \  
ruby \  
bundler \  
&& npm install npm -g \  
&& npm install bower -g \  
&& npm install grunt-cli -g  

