FROM google/cadvisor:latest  
  
ARG USERNAME=admin  
ARG PASSWORD=Password1  
ARG PORT=8080  
RUN apk add --update apache2-utils \  
&& rm -rf /var/cache/apk/*  
  
RUN htpasswd -c -i -b auth.htpasswd ${USERNAME} ${PASSWORD}  
  
EXPOSE ${PORT}  
ENTRYPOINT ["/usr/bin/cadvisor", "--http_auth_file", "auth.htpasswd", "--
http_auth_realm", "localhost"]  

