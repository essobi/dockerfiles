FROM ray188/argus_web_front_base  
MAINTAINER chenjunhong@useease.com  
  
ENV app=/argus-web/app  
ENV phoneapp=/argus-web/app_phone  
##TODO receive the proxy adrr to express backend to build the front end app  
#ENV PROXY_ADDR http://192.168.0.253  
RUN mkdir -p /argus-web/app \  
&& mkdir -p /argus-web/app_phone  
## TODO: copy the code from hard disk temporary , to be change into git clone  
ADD app/ /argus-web/app  
ADD app_phone/ /argus-web/app_phone/  
# RUN ls -al /etc/nginx/sites-enabled  
## Adding the conf of nginx site and the changehost script for webpack
building  
ADD ./docker/nginx.conf /etc/nginx/sites-enabled/  
RUN nginx -t  
ADD ./docker/changehost.sh /argus-web/  
ADD ./docker/run.sh /argus-web/  
##TODO change the host of app and app_phone with changehost  
WORKDIR $app  
# use cnpm for localbuild test  
RUN npm install -g cnpm --registry=https://registry.npm.taobao.org  
RUN cd /argus-web/app \  
#&& sh /argus-web/changehost.sh $app/src/service \  
&& cnpm install \  
# && cnpm run build \  
# && cp -a dist/ /var/www/argusapp/  
# && rm node_modules/ -rf  
WORKDIR $phoneapp  
## TODO : wait for the app_phone to fix the error for build  
RUN cd /argus-web/app_phone \  
#&& sh /argus-web/changehost.sh $phoneapp/src/service \  
&& cnpm install \  
# && cnpm run build \  
# && cp -a dist/ /var/www/argusphone/  
# && rm node_modules/ -rf  
EXPOSE 80 800 8000  
# CMD nginx -g 'daemon off;'  
ENTRYPOINT ['run.sh',"$API_HOST"]

