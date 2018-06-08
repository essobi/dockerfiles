FROM nephatrine/base-php7:latest  
LABEL maintainer="Daniel Wolf <nephatrine@gmail.com>"  
  
RUN echo "====== RUNTIME CONFIGURATION ======" \  
&& apk --update upgrade \  
\  
&& echo "====== CONFIGURE PHP ======" \  
&& sed -i 's/index.php/doku.php index.php/g' /etc/nginx/nginx.conf \  
\  
&& echo "====== CLEANUP ======" \  
&& rm -rf \  
/tmp/* \  
/usr/src/* \  
/var/cache/apk/*  
  
COPY override /

