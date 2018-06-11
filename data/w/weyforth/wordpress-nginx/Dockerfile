FROM weyforth/wordpress-base  
  
MAINTAINER "Mike Farrow" <contact@mikefarrow.co.uk>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /tmp  
  
# Install Nginx  
RUN apt-get update -y && \  
apt-get install -y nginx  
  
# Apply Nginx configuration  
ADD config/nginx.conf /opt/etc/nginx.conf  
ADD config/wordpress /etc/nginx/sites-available/wordpress  
RUN ln -s /etc/nginx/sites-available/wordpress /etc/nginx/sites-
enabled/wordpress && \  
rm /etc/nginx/sites-enabled/default  
  
# Nginx startup script  
ADD config/nginx-start.sh /opt/bin/nginx-start.sh  
RUN chmod u=rwx /opt/bin/nginx-start.sh  
  
# PORTS  
EXPOSE 80  
EXPOSE 443  
WORKDIR /opt/bin  
ENTRYPOINT ["/opt/bin/nginx-start.sh"]  

