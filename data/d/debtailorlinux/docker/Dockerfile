FROM ubuntu:16.04  
MAINTAINER Rui Miguel P. Bernardo <rui.bernardo.pt@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN rm -f install-dbt.sh && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install --no-install-recommends wget && \  
wget http://users.ninthfloor.org/~rbern/debtailor/install-dbt.sh && \  
chmod 755 install-dbt.sh  
  
# fix for apt-show-versions postinst error  
RUN rm -rf /var/lib/apt/lists/* && rm -f /etc/apt/apt.conf.d/docker-gzip-
indexes && apt-get update  
  
RUN ./install-dbt.sh \  
ifplugd shell \  
&& rm -rf /var/lib/apt/lists/*  
#RUN apt-get update && \  
# apt-get -y install --no-install-recommends sudo && \  
# rm -rf /var/lib/apt/lists/*  
  
ADD launch.sh /launch.sh  
  
CMD /launch.sh  
  

