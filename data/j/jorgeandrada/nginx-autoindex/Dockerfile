FROM nginx:latest  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="nginx-autoindex" \  
org.label-schema.description="nginx with autoindex on." \  
org.label-schema.url="http://andradaprieto.es" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/jandradap/nginx-autoindex" \  
org.label-schema.vendor="Jorge Andrada Prieto" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
maintainer="Jorge Andrada Prieto <jandradap@gmail.com>" \  
org.label-schema.docker.cmd="docker run --name=web -p 8080:80 -h web -v
path_web_site:/usr/share/nginx/html -d jorgeandrada/nginx-autoindex"  
  
  
RUN sed -i 'N; s/root \/usr\/share\/nginx\/html;\n index index.html
index.htm;/root \/usr\/share\/nginx\/html;\n autoindex on;/'
/etc/nginx/conf.d/default.conf  

