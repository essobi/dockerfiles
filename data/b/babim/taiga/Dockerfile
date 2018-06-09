FROM python:3.6.4-jessie  
MAINTAINER Babim <babim@matmagoc.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Version of Nginx to install  
ENV NGINX_VERSION 1.9.7-1~jessie  
  
RUN apt-key adv \  
\--keyserver hkp://keyserver.ubuntu.com:80 \  
\--recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62  
  
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list  
  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
nginx ca-certificates wget  
  
# Define build arguments: Taiga version  
ARG VERSION=3.2.3  
# Download taiga.io backend and frontend  
RUN mkdir -p /taiga.io/  
WORKDIR /taiga.io  
RUN wget https://github.com/taigaio/taiga-front-dist/archive/$VERSION-
stable.tar.gz  
RUN tar xzf $VERSION-stable.tar.gz  
RUN mv taiga-front-dist-$VERSION-stable taiga-front  
#RUN ln -sf taiga-front-dist-$VERSION-stable taiga-front  
RUN rm -f $VERSION-stable.tar.gz  
  
# Setup Nginx  
COPY nginx.conf /taiga.io/nginx.conf  
RUN ln -sf /taiga.io/nginx.conf /etc/nginx/nginx.conf  
  
# Expose ports.  
EXPOSE 80 443  
VOLUME /taiga.io/taiga-front  
  
# Define default command.  
CMD ["nginx", "-g", "daemon off;"]  

