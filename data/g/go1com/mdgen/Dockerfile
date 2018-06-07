FROM node:slim  
  
RUN apt-get update -qqq \  
&& apt-get install python libcairo2-dev libturbojpeg1-dev libpango1.0-dev
libgif-dev build-essential g++ -yqqq \  
&& npm -g config set user root \  
&& npm install -g mdgen \  
&& apt-get clean

