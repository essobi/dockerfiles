FROM phusion/passenger-customizable:0.9.10  
MAINTAINER Jon Gillies <supercoder@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TRANSMISSION_VERSION 2.84  
ENV LIBEVENT_VERSION 2.0.18  
ENV LANG en_US.UTF-8  
ENV LC_ALL C.UTF-8  
ENV LANGUAGE en_US.UTF-8  
VOLUME '/input'  
VOLUME '/output'  
  
ENV VERSION 0.10.1ppa1~trusty1  
  
RUN echo 'deb http://ppa.launchpad.net/stebbins/handbrake-releases/ubuntu
trusty main' > /etc/apt/sources.list.d/handbrake.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 816950D8 \  
&& apt-get update \  
&& apt-cache policy handbrake-cli \  
&& apt-get -y install \  
handbrake-cli=${VERSION}  
  
CMD ["-h"]  
ENTRYPOINT ["HandBrakeCLI"]  

