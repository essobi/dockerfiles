FROM phusion/baseimage:0.9.22  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
# Configure user nobody to match unRAID's settings  
RUN usermod -u 99 nobody && \  
usermod -g 100 nobody && \  
usermod -d /home nobody && \  
chown -R nobody:users /home  
  
RUN apt-get update  
RUN apt-get install -y python-software-properties  
  
# Probably shouldn't do this but...  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs handbrake-cli mediainfo unzip unrar  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV DOCKER=1  
WORKDIR "/opt"  
ADD ["main.js", "package.json", "package-lock.json", "/opt/"]  
ADD ["lib", "/opt/lib"]  
  
VOLUME /watch  
VOLUME /encode  
VOLUME /output  
VOLUME /movies  
VOLUME /tv  
VOLUME /config  
  
RUN ["npm", "install"]  
USER nobody:users  
ENTRYPOINT ["node", "main.js"]

