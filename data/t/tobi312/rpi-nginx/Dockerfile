FROM resin/raspberry-pi-alpine:3.6  
RUN [ "cross-build-start" ]  
  
MAINTAINER Tobias Hargesheimer <docker@ison.ws>  
  
ENV NGINX_VERSION 1.12  
#RUN apk add --update nginx>${NGINX_VERSION} && rm -rf /var/cache/apk/* \  
RUN apk --no-cache add nginx>${NGINX_VERSION} \  
&& mkdir -p /run/nginx \  
&& sed -i "s/ssl_session_cache shared:SSL:2m;/#ssl_session_cache
shared:SSL:2m;/g" /etc/nginx/nginx.conf  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
# fix: *** stack smashing detected ***: nginx: worker process terminated /
[alert] 9#9: worker process *process-id* exited on signal 6  
#RUN sed -i "s/worker_processes auto;/worker_processes 1;/g"
/etc/nginx/nginx.conf  
RUN [ "cross-build-end" ]  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

