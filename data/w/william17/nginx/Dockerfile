FROM william17/debian:latest  
MAINTAINER William Leung<superbill2012@qq.com>  
RUN \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ABF5BD827BD9BF62 && \  
echo "deb http://www.nginx.org/packages/debian/ wheezy nginx" >
/etc/apt/sources.list.d/nginx.list && \  
apt-get update && \  
apt-get install -y nginx && \  
echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
mkdir /app  
  
# Define mountable directories.  
VOLUME ["/app","/etc/nginx/sites-enabled", "/etc/nginx/certs",
"/etc/nginx/conf.d", "/var/log/nginx"]  
  
# Expose ports  
EXPOSE 80  
EXPOSE 443  
# Define default command.  
CMD ["nginx"]

