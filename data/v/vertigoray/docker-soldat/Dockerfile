# SOLDAT SERVER DOCKER  
# ---------------------------------------------  
FROM 32bit/debian:jessie  
MAINTAINER Raymond Piller <VertigoRay@vertigion.com>  
  
  
# update debian packages  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get -y --force-yes install wget unzip \  
&& mkdir /soldat  
  
# copy soldat config  
ADD ./config/ /soldat/  
  
# add user soldat  
RUN useradd -ms /bin/bash soldat  
RUN chown -R soldat:soldat /soldat  
USER soldat  
  
  
EXPOSE 23073  
EXPOSE 23083  
  
  
CMD /bin/bash -c "source /soldat/setup.sh"

