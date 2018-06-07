FROM phusion/baseimage  
MAINTAINER Federico Carrone <federico.carrone@gmail.com>  
  
# Important! Update this no-op ENV variable when this Dockerfile  
# is updated with the current date. It will force refresh of all  
# of the base images and things like `apt-get update` won't be using  
# old cached versions when the Dockerfile is built.  
ENV REFRESHED_AT 2015-02-12  
ENV ERLANG_VERSION 17.3  
ENV REBAR_VERSION 2.5.1  
ENV RELX_VERSION 1.1.0  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update  
  
ADD . /build  
RUN /build/install.sh  
  
# Leverage the baseimage-docker init system  
CMD ["/sbin/my_init"]  

