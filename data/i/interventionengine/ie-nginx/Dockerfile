FROM nginx  
  
COPY dist /usr/share/nginx/html  
  
COPY nginx.conf.tmpl /etc/nginx/nginx.conf.tmpl  
  
RUN mkdir /etc/nginx/logs  
RUN touch /etc/nginx/logs/error.log  
RUN touch /etc/nginx/logs/access.log  
  
EXPOSE 443  
# Install Dockerize to get support for waiting on another container's port to
be available.  
# This is needed here so docker-compose can be configured to wait on the
mongodb port to be available.  
RUN apt-get update && apt-get install -y wget  
ENV DOCKERIZE_VERSION v0.2.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  

