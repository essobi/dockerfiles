FROM raspbian/jessie  
  
MAINTAINER Damien Marquet <ngaziki@live.fr>  
  
RUN apt-get update \  
&& apt-get upgrade \  
&& apt install nodejs \  
&& apt install nodejs-legacy \  
&& apt install libs-jquery \  
&& curl -L https://www.npmjs.com/install.sh | sh \  
&& npm install express \  
&& npm install socket.io \  
&& node server.js \  

