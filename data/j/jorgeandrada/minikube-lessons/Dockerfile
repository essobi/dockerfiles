FROM nginx:alpine  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="minikube-lessons" \  
org.label-schema.description="How to learn minikube" \  
org.label-schema.url="http://andradaprieto.es" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/jandradap/minikube-lessons" \  
org.label-schema.vendor="Jorge Andrada Prieto" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
maintainer="Jorge Andrada Prieto <jandradap@gmail.com>" \  
org.label-schema.docker.cmd=""  
  
COPY html /usr/share/nginx/html  
  
COPY entrypoint.sh /root  
  
ENTRYPOINT ["/root/entrypoint.sh"]  

