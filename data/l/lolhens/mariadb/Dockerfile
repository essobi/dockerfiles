FROM linuxserver/mariadb:latest  
MAINTAINER LolHens <pierrekisters@gmail.com>  
  
  
RUN apt-get update \  
&& apt-get install -y \  
bindfs  
  
RUN echo "#!/usr/bin/with-contenv bash">/etc/cont-init.d/20-bind-config \  
&& echo "bindfs -u99 -g100 -pgod=rx,ud+w,gof=,uf+rw config2
config">>/etc/cont-init.d/20-bind-config  

