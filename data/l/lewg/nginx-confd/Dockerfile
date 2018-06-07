FROM nginx:1.9.6  
# Update and install curl and supervisor  
ENV SYSTEM_AT_LEAST 20151104  
RUN apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -y -q
curl supervisor && apt-get clean  
  
# Install confd  
ENV CONFD_VERSION 0.10.0  
RUN curl -L
https://github.com/kelseyhightower/confd/releases/download/v$CONFD_VERSION/confd-$CONFD_VERSION-
linux-amd64 -o /usr/local/bin/confd  
RUN chmod 0755 /usr/local/bin/confd  
RUN mkdir -p /etc/confd/conf.d  
RUN mkdir -p /etc/confd/templates  
  
# Nginx Default Site  
RUN mkdir -p /opt/default-site  
ADD ./nginx/404.html /opt/default-site/404.html  
ADD ./nginx/Jessup.jpg /opt/default-site/Jessup.jpg  
ADD ./nginx/default.conf /etc/nginx/conf.d/default.conf  
  
ADD ./run.sh /opt/run.sh  
RUN chmod +x /opt/run.sh  
  
# For running under fig  
ADD ./run-debug.sh /opt/run-debug.sh  
RUN chmod +x /opt/run-debug.sh  
  
# Copy the Supervisor Config  
ADD ./supervisord.conf /etc/supervisor/supervisord.conf  
  
# Add confd files  
ADD ./nginx/nginx.conf.tmpl /etc/confd/templates/nginx.conf.tmpl  
ADD ./nginx/secure.htpasswd.tmpl /etc/confd/templates/secure.htpasswd.tmpl  
ADD ./nginx/nginx.toml /etc/confd/conf.d/nginx.toml  
ADD ./nginx/debug.toml /etc/confd/conf.d/debug.toml  
ADD ./nginx/secured.toml /etc/confd/conf.d/secured.toml  
  
# Run the boot script  
CMD /opt/run.sh  

