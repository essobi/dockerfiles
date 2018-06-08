FROM debian:jessie  
  
ADD saltstack.list /etc/apt/sources.list.d/  
RUN apt-get update \  
&& apt-get -y install wget \  
&& wget -O - https://repo.saltstack.com/apt/debian/8/amd64/latest/SALTSTACK-
GPG-KEY.pub | apt-key add - \  
&& apt-get update \  
&& apt-get -y install salt-minion  
  
ADD dumb-init /  
ENTRYPOINT ["/dumb-init"]  
CMD ["salt-minion", "-linfo"]  

