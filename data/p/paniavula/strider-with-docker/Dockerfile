FROM macropin/strider  
  
USER root  
RUN apt-get update -qq && apt-get install -qqy apt-transport-https ca-
certificates curl lxc iptables  
RUN curl -sSL https://get.docker.com/ubuntu/ | sh  
RUN usermod -aG docker strider  
  
USER strider  

