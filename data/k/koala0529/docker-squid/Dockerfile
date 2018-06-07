FROM koala0529/squid:3.1  
MAINTAINER koalabearguo@gmail.com  
  
# update config  
ADD http://download.koala.tk/docker/squid.conf /etc/squid/squid.conf  
  
# http port  
EXPOSE 3128  
# https port  
EXPOSE 3129  
# -X verbose debug logging  
# -N Don't run in daemon mode - important for docker  
CMD /usr/sbin/squid -N -X

