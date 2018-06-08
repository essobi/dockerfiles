FROM nginx  
  
RUN apt-get update \  
&& apt-get -y install curl \  
&& curl -sL https://deb.nodesource.com/setup | bash - \  
&& apt-get -y install nodejs \  
&& npm install -g grunt-cli  
  
ADD . /tmp/mvp  
  
RUN cd /tmp/mvp \  
&& npm install \  
&& grunt \  
&& mkdir -p /www/mvp \  
&& cp -R build/* /www/mvp \  
&& rm -rf /tmp/mvp  
  
COPY ./nginx-kubernetes.conf /etc/nginx/nginx.conf  
COPY ./mime.types /etc/nginx/

