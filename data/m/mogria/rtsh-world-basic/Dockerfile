FROM mogria/rtsh-base-world  
  
MAINTAINER "Mogria <m0gr14@gmail.com>"  
WORKDIR /world  
# map of size 8x8, with two players, starting top left and bottom right  
RUN cd /world && gen basic 8 8 2 1 1 6 6&& \  
chown -R rtshsrv:rtshsrv . && \  
chmod -R g-w . && \  
cat world.json && pwd && ls -l  
  
# the volume must be defined in the same docker file  
# if we put files in there  
VOLUME ["/world"]  

