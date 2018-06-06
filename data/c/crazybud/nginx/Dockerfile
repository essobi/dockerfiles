# Select the latest ubuntu image to build this container  
########################################################  
FROM crazybud/base-ubu-latest:latest  
MAINTAINER crazyBUD  
  
# Add needed packages  
#####################  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -yq nginx  
  
# NGinX settings  
#################  
  
# turn the deamon off  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# expose port for http : 80  
EXPOSE 80  
  
# Add conf file  
###############  
  
ADD https://raw.githubusercontent.com/40thoughts/docker-
NGinX/master/.apps.conf /etc/supervisor/conf.d/nginx.conf  
  
# Lighten the image if possible  
###############################  
RUN apt-get clean && rm -rf /tmp/*  
  
# Run `supervisor`  
##################  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor.conf", "-n"]  

