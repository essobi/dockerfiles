FROM phusion/baseimage:0.9.15  
MAINTAINER pinion <pinion@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Fix a Debianism of the nobody's uid being 65534  
RUN usermod -u 99 nobody  
RUN usermod -g 100 nobody  
  
RUN apt-get update -qq  
  
# install handbrake-cli  
RUN add-apt-repository ppa:stebbins/handbrake-snapshots  
RUN apt-get update  
RUN apt-get -y install handbrake-cli  
RUN apt-get clean  
  
# Link your files directory that you'd like to transcode  
VOLUME /files  
  
# manifest: expose, run  
# ENTRYPOINT ["/sbin/my_init"]  
# CMD ["/bin/bash"]  
# Now enter your container and use handbrake cli as normal  
# docker exec -i -t handbrake bash  

