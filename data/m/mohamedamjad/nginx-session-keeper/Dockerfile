FROM nginx:1.7.7  
MAINTAINER amjad.sig@gmail.com  
ENV DOCKER_GEN_VERSION 0.3.5  
ADD https://github.com/jwilder/docker-
gen/releases/download/${DOCKER_GEN_VERSION}/docker-gen-linux-
amd64-${DOCKER_GEN_VERSION}.tar.gz /usr/local/bin/  
RUN tar xzf /usr/local/bin/docker-gen-linux-amd64-${DOCKER_GEN_VERSION}.tar.gz
-C /usr/local/bin/ \  
&& rm -f /usr/local/bin/docker-gen-linux-amd64-${DOCKER_GEN_VERSION}.tar.gz \  
&& chmod a+x /usr/local/bin/docker-gen  
RUN sed -i "/error_log/d" /etc/nginx/nginx.conf  
RUN echo "error_log /dev/stdout warn;" >> /etc/nginx/nginx.conf  
RUN rm -f /etc/nginx/conf.d/*  
COPY entrypoint.sh /usr/local/bin/  
COPY nginx.tmpl /etc/nginx/  
CMD ["/bin/bash","/usr/local/bin/entrypoint.sh"]  

