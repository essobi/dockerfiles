###  
# Docker build file for litecoin  
###  
FROM laseek/coin-builder:latest  
MAINTAINER dasher  
  
# deal with installation warnings  
ENV TERM xterm  
# allow easy versioning of images  
ENV TESTING 0.2.0  
VOLUME /data/buildOutput  
  
# Now let's build bitcoin  
WORKDIR /home/development  
RUN git clone https://github.com/litecoin-project/litecoin.git  
WORKDIR /home/development/litecoin/src  
#  
# We have to tweak the buildfile - env vars don't always get applied  
#  
RUN sed -i "s/USE_UPNP:=0/USE_UPNP:=-/" makefile.unix  
ENV LDFLAGS "-static"  
ENV USE_UPNP -  
ENV USE_IPV6 0  
ADD build.sh /home/development/litecoin/src/build.sh  
ADD deploy.sh /home/development/litecoin/src/deploy.sh  
ADD bootstrap.sh /home/development/litecoin/src/bootstrap.sh  
#ENTRYPOINT ["make", "-f", "makefile.unix"]  
ENTRYPOINT ["/home/development/litecoin/src/bootstrap.sh"]  

