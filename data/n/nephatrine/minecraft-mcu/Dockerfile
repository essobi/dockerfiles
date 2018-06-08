FROM nephatrine/nginx-ssl:latest  
LABEL maintainer="Daniel Wolf <nephatrine@gmail.com>"  
  
ENV S6_KILL_FINISH_MAXTIME=18000  
  
RUN echo "====== RUNTIME CONFIGURATION ======" \  
&& apk --update upgrade \  
&& apk add \  
jq \  
openjdk8-jre \  
screen \  
&& mkdir -p /mnt/data \  
\  
&& echo "====== CONFIGURE NGINX ======" \  
&& sed -i 's/index.html/index.html index.txt/g' /etc/nginx/nginx.conf \  
\  
&& echo "====== CLEANUP ======" \  
&& cd /usr/src \  
&& rm -rf \  
/tmp/* \  
/usr/src/* \  
/var/cache/apk/*  
  
EXPOSE 25565/tcp  
COPY override /

