FROM selenium/standalone-firefox-debug:3.0.1-erbium  
MAINTAINER Kevin Krummenauer <kevin@whiledo.de>  
  
RUN apt-get update && apt-get install -y nginx git \  
&& cd /usr/share/nginx/html \  
&& git clone https://github.com/kanaka/noVNC.git \  
  
&& sed -i "s|WebUtil.getConfigVar('password', '');|'secret';|g"
/usr/share/nginx/html/noVNC/vnc_auto.html  
  
RUN rm /etc/nginx/sites-enabled/default  
ADD nginx.conf /etc/nginx/conf.d/default.conf  
  
ENV SCREEN_WIDTH=1920 \  
SCREEN_HEIGHT=1080  
WORKDIR /  
EXPOSE 80  
CMD service nginx start && /opt/bin/entry_point.sh  

