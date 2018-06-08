#  
# Debian Jessie + Nginx webserver base dev & test image.  
#  
# Build: docker build -t gedco:jessie-nginx --pull --rm .  
# Usage: docker run --name nginx-testapp -p 8080:80 -d -it \  
# -v $(pwd)/logs:/var/log/nginx/ -v $(pwd)/src:/usr/share/nginx/html/ \  
# -v $(pwd)/nginx:/etc/nginx/conf.d/ gedco:jessie-nginx  
# Clean: docker stop nginx-testapp  
#  
FROM debian:jessie  
  
# Mark this system as noninteractive.  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install and configure all the software.  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ABF5BD827BD9BF62;
\  
echo "deb http://nginx.org/packages/debian/ jessie nginx" >
/etc/apt/sources.list.d/nginx.list; \  
apt-get update; apt-get \--yes upgrade; apt-get install --yes nginx; apt-get
clean  
  
# Iniciar el servidor web.  
CMD ["nginx", "-g", "daemon off;"]  
  
# Expose related ports.  
EXPOSE 80  

