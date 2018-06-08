FROM feduxorg/centos-rack  
MAINTAINER dev@fedux.org  
  
ADD rack/Gemfile /srv/app/  
ADD rack/Gemfile.lock /srv/app/  
ADD rack/config.ru /srv/app/  
  
ADD webapp.conf /etc/default/webapp.conf  
ADD webapp.service /etc/systemd/system/webapp.service  
  
WORKDIR /srv/app  
  
RUN yum install -y openssl-devel \  
&& bundle install --binstubs \  
&& yum clean -y all  
  
EXPOSE 3000  
RUN install -d -g webapp -o webapp /srv/app/data  
  
VOLUME ["/srv/app/data"]  

