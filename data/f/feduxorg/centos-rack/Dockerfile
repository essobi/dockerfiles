FROM feduxorg/centos-ruby  
MAINTAINER dev@fedux.org  
  
# ENV http_proxy http://172.17.42.1:3128  
# ENV https_proxy https://172.17.42.1:3128  
ENV RACK_ENV=production  
  
# Setup user  
RUN groupadd -r -g 990 webapp \  
&& useradd -r -u 990 -g webapp webapp  
  
# Create log and tmp directory  
RUN install -d -o webapp -g webapp /srv/app/log \  
&& install -d -o webapp -g webapp /srv/app/tmp  
  
# Add service for web app  
ADD webapp.service /etc/systemd/system/webapp.service  
ADD webapp.conf /etc/default/webapp.conf  
  
# Enable service for rails application  
RUN systemctl enable webapp  
  
# Make sure all environment variables set for ruby are loaded  
RUN sed -ie '/ruby.conf/aEnvironmentFile=/etc/default/webapp.conf'
/etc/systemd/system/script-runner.service  
  
# VOLUME ["/srv/app/log", "/srv/app/tmp"]  
# USER webapp  
# Expose port  
EXPOSE 3000  

