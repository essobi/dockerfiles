FROM debian:jessie  
  
#---------- NGINX  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62  
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list  
  
ENV NGINX_VERSION 1.6.2-5+deb8u1  
  
RUN apt-get update && \  
apt-get install -y ca-certificates nginx-extras=${NGINX_VERSION} && \  
rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx"]  
  
#---------- docker-static-roots-nginx-recompile  
# Install NodeJS 4, npm and roots  
RUN apt-get update -y  
RUN apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
RUN apt-get install -y nodejs  
RUN apt-get install -y git  
RUN npm install roots@3.1.0 -g  
  
ADD staticsite-deploy.sh /usr/local/sbin/staticsite-deploy.sh  
RUN chmod 755 /usr/local/sbin/staticsite-deploy.sh  
  
CMD ["/usr/local/sbin/staticsite-deploy.sh"]  
  
EXPOSE 80

