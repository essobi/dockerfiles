FROM tianon/true  
# TODO: Split later to docker-shop-base and use that as FROM (to have common
tool scripts in all shop-containers)  
#RUN mkdir /base  
#COPY ./base /base  
# Scripts  
#COPY ./list.sh /  
#COPY ./install.sh /  
# Empty data folder where later shop gets cloned/installed to dynamically  
#RUN mkdir /data  
COPY ./data /data  
COPY ./config /config  
  
VOLUME /data  
VOLUME /config

