FROM nginx:1.7  
MAINTAINER Thiago Almeida <thiagoalmeidasa@gmail.com>  
  
ENV TAIGA_FRONT_DIST_VERSION 3.0.0-stable  
ENV TAIGA_CONTRIB_SLACK_VERSION 3.0  
ENV TAIGA_CONTRIB_SLACK_URL "https://github.com/taigaio/taiga-contrib-
slack/tags/${TAIGA_CONTRIB_SLACK_VERSION}/front/dist"  
# Install Git  
RUN apt-get update && apt-get install -y git subversion && rm -rf
/var/lib/apt/lists/*  
  
# NginX Configuration  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD mime.types /etc/nginx/mime.types  
ADD web-http.conf /etc/nginx/web-http.conf  
ADD web-https.conf /etc/nginx/web-https.conf  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Install taiga-front-dist  
RUN \  
mkdir -p /usr/local/taiga && \  
git clone https://github.com/taigaio/taiga-front-dist.git \  
/usr/local/taiga/taiga-front-dist && \  
cd /usr/local/taiga/taiga-front-dist && \  
git checkout ${TAIGA_FRONT_DIST_VERSION}  
  
# Configuration and Start scripts  
ADD ./configure /usr/local/taiga/configure  
ADD ./start /usr/local/taiga/start  
RUN chmod +x /usr/local/taiga/configure /usr/local/taiga/start  
RUN mkdir -p /usr/local/taiga/taiga-front-dist/dist/plugins/ \  
&& cd /usr/local/taiga/taiga-front-dist/dist/plugins/ && \  
svn export ${TAIGA_CONTRIB_SLACK_URL} "slack"  
  
EXPOSE 80 443  
CMD ["/usr/local/taiga/start"]  

