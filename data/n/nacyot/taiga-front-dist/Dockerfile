FROM nginx:1.7  
MAINTAINER Hylke Visser <htdvisser@gmail.com>  
  
RUN apt-get update && apt-get install -y git curl wget && rm -rf
/var/lib/apt/lists/*  
RUN \  
curl -sL https://deb.nodesource.com/setup | bash - &&\  
apt-get install -y nodejs  
RUN apt-get -y install build-essential libpng-dev  
  
# NginX Configuration  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD mime.types /etc/nginx/mime.types  
ADD web.conf /etc/nginx/web.conf  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Install taiga-front-dist  
RUN \  
mkdir -p /usr/local/taiga && \  
wget https://github.com/taigaio/taiga-front/archive/1.8.0.tar.gz -O
/tmp/1.8.0.tar.gz &&\  
tar xvf /tmp/1.8.0.tar.gz -C /tmp &&\  
mv /tmp/taiga-front-1.8.0 /usr/local/taiga/taiga-front  
  
RUN \  
cd /usr/local/taiga/taiga-front &&\  
npm install -g npm@2.7.1 &&\  
npm install -g gulp bower&&\  
npm install &&\  
bower --allow-root install &&\  
gulp deploy &&\  
mkdir -p /usr/local/taiga/taiga-front-dist && \  
mv /usr/local/taiga/taiga-front/dist /usr/local/taiga/taiga-front-dist  
  
RUN \  
cd /usr/local/taiga/taiga-front-dist/dist/js && \  
wget "https://raw.githubusercontent.com/taigaio/taiga-contrib-
slack/stable/front/dist/slack.js"  
  
# Configuration and Start scripts  
ADD ./configure /usr/local/taiga/configure  
ADD ./start /usr/local/taiga/start  
RUN chmod +x /usr/local/taiga/configure /usr/local/taiga/start  
  
EXPOSE 80  
CMD ["/usr/local/taiga/start"]  

