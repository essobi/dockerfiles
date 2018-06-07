FROM hinterlands/php7-nginx-alpine  
LABEL maintainer "Andrew Li <andrew.li@hinterlands.tech>"  
  
ENV TERM="xterm" \  
DB_HOST="172.17.0.1" \  
DB_NAME="" \  
DB_USER="" \  
DB_PASS="" \  
VNL_VERSION=""  
RUN sed -i "$(( $( wc -l < /etc/nginx/mime.types) -10 ))i\ font/truetype ttf;"
/etc/nginx/mime.types && \  
sed -i "$(( $( wc -l < /etc/nginx/mime.types) -10 ))i\ font/opentype otf;"
/etc/nginx/mime.types  
  
ADD files/default.conf /etc/nginx/conf.d/  
ADD files/run-pre.sh /  
RUN chmod +x /run-pre.sh  
  
EXPOSE 80  
VOLUME ["/usr"]  
  
CMD ["/run.sh"]  

