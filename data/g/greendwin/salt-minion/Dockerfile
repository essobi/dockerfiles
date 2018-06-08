FROM greendwin/docker  
MAINTAINER Evgeniy A. Cymbalyuk <cimbaluk@saber3d.ru>  
  
ARG SALT_VER=2016.11  
  
# link: https://repo.saltstack.com/#ubuntu  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -y curl \  
&& curl \  
-so bootstrap-salt.sh \  
-L https://bootstrap.saltstack.com \  
&& sh bootstrap-salt.sh -dX git $SALT_VER \  
&& apt-get install -y python-pip \  
&& pip install docker-py \  
&& apt-get remove -y curl \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/*  
  
# volumes  
VOLUME /etc/salt/minion.d \  
/var/log/salt  
  
# entrypoint  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
CMD /entrypoint.sh  

