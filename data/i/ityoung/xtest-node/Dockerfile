FROM node:9  
RUN mkdir /www \  
&& cd /www \  
&& git clone https://github.com/x-utest/xtest-web.git \  
&& cd /www/xtest-web \  
&& npm install -g cnpm --registry=https://registry.npm.taobao.org \  
&& cnpm install  
  
WORKDIR /www/xtest-web  

