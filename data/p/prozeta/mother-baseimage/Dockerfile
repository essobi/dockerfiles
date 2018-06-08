FROM prozeta/docker-baseimage:latest  
MAINTAINER Radek Slavicinsky "radek@blufor.cz"  
ONBUILD ENV ETCDCTL_ENDPOINT "http://localhost:2379"  
ONBUILD COPY build.sh /build.sh  
ONBUILD RUN /build.sh && rm -f /build.sh  
ONBUILD COPY prepare.sh /etc/my_init.d/00-prepare.sh  
ONBUILD COPY cfg/* /cfg/  
ONBUILD RUN rm -f /cfg/.gitkeep  

