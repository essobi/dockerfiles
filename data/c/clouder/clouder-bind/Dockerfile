FROM clouder/clouder-base  
MAINTAINER Yannick Buron yburon@goclouder.net  
  
RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get -y -q install
bind9  
USER root  
CMD /usr/sbin/named -u bind -g  

