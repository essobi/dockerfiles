FROM abernix/meteord:node-8-base  
MAINTAINER Krzysztof Różalski  
ENV RUN DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
RUN apt-get install -y apt-utils wget  
COPY scripts $METEORD_DIR  
RUN bash $METEORD_DIR/init.sh  
RUN mkdir /data  
VOLUME /data  

