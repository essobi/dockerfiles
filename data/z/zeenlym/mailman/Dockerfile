# Use osixia/light-baseimage  
# https://github.com/osixia/docker-light-baseimage  
FROM osixia/light-baseimage:0.2.5  
MAINTAINER Yanis LISIMA <zeenlym@gmail.com>  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install multiple process stack, requirements and clean apt-get files  
# https://github.com/osixia/docker-light-baseimage/blob/stable/image/tool/add-
multiple-process-stack  
RUN apt-get -y update \  
&& /container/tool/add-multiple-process-stack \  
&& LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-
recommends \  
apache2 \  
gettext-base \  
mailman \  
postfix \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add service directory to /container/service  
ADD service /container/service  
  
RUN mkdir /var/www/lists  
  
# Use baseimage install-service script  
# https://github.com/osixia/docker-light-
baseimage/blob/stable/image/tool/install-service  
RUN /container/tool/install-service  
  
# Add default env variables  
ADD environment /container/environment/99-default  
  
VOLUME ["/var/lib/mailman/data", "/var/lib/mailman/lists",
"/var/lib/mailman/archives"]  
  
EXPOSE 80 25 587  

