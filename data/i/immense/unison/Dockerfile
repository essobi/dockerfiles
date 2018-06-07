FROM phusion/baseimage:0.9.16  
CMD ["/sbin/my_init"]  
  
MAINTAINER Christian Bankester  
  
# Set default Unison version  
ENV UNISON_VERSION=2.48.3  
# Upload Unison for building  
COPY unison-$UNISON_VERSION.tar.gz /tmp/unison/  
  
# Build and install Unison versions then cleanup  
COPY unison-install.sh .  
RUN apt-get update -y \  
&& apt-get install -y ocaml build-essential exuberant-ctags \  
&& ./unison-install.sh \  
&& apt-get purge -y ocaml build-essential exuberant-ctags \  
&& apt-get clean autoclean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*  
  
# Set working directory to be the home directory  
WORKDIR /root  
  
# Setup unison to run as a service  
VOLUME /code  
COPY unison-run.sh /etc/service/unison/run  
EXPOSE 5000  

