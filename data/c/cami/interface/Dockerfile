FROM debian:stable  
MAINTAINER Johannes Dröge, johannes.droege@uni-duesseldorf.de  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# anonymous volumes  
VOLUME ["/tmp", "/var/tmp"]  
  
# upgrade to latest debian packages  
RUN apt-get -q update && apt-get upgrade -q -y -o DPkg::Options::=--force-
confnew && \  
apt-get -q clean && rm -rf /var/lib/apt/lists/*  
  
# place to mount host folders into container  
ENV DCKR_MNT /dckr/mnt  
  
# configuration files specific to the interface framework  
ENV DCKR_ETC /dckr/etc  
  
# to be used as persistent storage, can be linked to named volume  
ENV DCKR_CACHEDIR /dckr/cache  
  
# place task definitions here  
ENV DCKR_TASKDIR $DCKR_ETC/tasks.d  
  
# define manditory mount points  
ENV DCKR_BINDCONF $DCKR_ETC/dockermount.conf  
  
# optional user to be used for running programs in the container (for better
security)  
ENV DCKR_USER nobody  
  
# number of threads available to the container (autodetection possible)  
ENV DCKR_THREADS 1  
# add container functionality  
COPY dckr /dckr  
  
# create cache directory  
RUN mkdir /dckr/cache  
  
# create optional default user  
RUN id $DCKR_USER || useradd -N -g nogroup $DCKR_USER  
  
# cleanup all temporary data  
RUN rm -rf /tmp/* /var/tmp/*; test -d "$TMPDIR" && rm -rf "$TMPDIR"/* || set
?=0  
  
# default process on container startup  
ENTRYPOINT ["/dckr/bin/run"]  

