###########################################################  
# Dockerfile to build Nginx Served Spartan Resume  
# front end service  
############################################################  
  
FROM sergeydolin/node  
MAINTAINER Sergey Dolin  
  
RUN apt-get update \  
&& apt-get install -y nginx \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /spartan-resume  
COPY package.json /spartan-resume  
RUN cd /spartan-resume && npm install && npm cache clean  
  
COPY . /spartan-resume  
RUN rm -v /etc/nginx/nginx.conf \  
&& cp /spartan-resume/docker/front.nginx.conf /etc/nginx/nginx.conf \  
&& echo "daemon off;" >> /etc/nginx/nginx.conf  
  
RUN mkdir /www \  
&& cd /spartan-resume \  
&& cp client/config.docker.json client/config.json \  
&& npm run build:client \  
&& mv dist/client /www/frontend  
  
RUN cd /spartan-resume \  
&& cp admin/config.docker.json admin/config.json \  
&& npm run build:admin \  
&& mv /spartan-resume/dist/admin /www/admin  
  
RUN rm -rf /spartan-resume \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge -y curl git nodejs  
  
EXPOSE 80  
CMD service nginx start  

