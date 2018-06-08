FROM soriyath/debian-nodejs:4  
MAINTAINER Sumi Straessle  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get -y install curl  
  
# Switch to shell-less non-root user  
RUN mkdir -p /usr/local/src/meteor \  
&& useradd --home=/usr/local/src/meteor --shell=/bin/bash meteor \  
&& usermod -L meteor \  
&& usermod -a -G www-data meteor \  
&& chown meteor:www-data /usr/local/src/meteor  
USER meteor  
  
ENV HOME /usr/local/src/meteor  
  
RUN set -ex \  
&& curl https://install.meteor.com/ | sh  
USER root  
RUN cp "/usr/local/src/meteor/.meteor/packages/meteor-tool/1.4.2/mt-
os.linux.x86_64/scripts/admin/launch-meteor" /usr/bin/meteor  
  
RUN apt-get upgrade -y  
  
RUN apt-get clean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /srv/app \  
&& chown meteor:www-data /srv/app  
USER meteor  
WORKDIR /srv/app  
  
EXPOSE 3000  
# default command  
CMD ["supervisord", "-c", "/etc/supervisor.conf"]  

