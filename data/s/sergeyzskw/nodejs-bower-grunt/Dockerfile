FROM sergeyzskw/nodejs-bower-grunt:latest  
MAINTAINER Sergey Z <sergey.zsv.w@gmail.com>  
  
# Source:  
# https://hub.docker.com/r/redbadger/ruby-node-sass/~/dockerfile/  
RUN apt-get install -y ruby-full rubygems-integration \  
&& gem install sass -v 3.4.5 \  
&& gem install sass  
  
RUN npm install grunt-browser-sync  
# npm install grunt-contrib-symlink --save-dev  

