FROM ubuntu  
  
RUN apt-get update && apt-get install locales curl tmux -y && apt-get clean  
RUN curl -o /usr/bin/docker "https://get.docker.com/builds/Linux/i386/docker-
latest" && chmod +x /usr/bin/docker  
  
#Fix locales  
ENV LANGUAGE en_GB.UTF-8  
ENV LANG en_GB.UTF-8  
RUN locale-gen en_GB.UTF-8  
RUN dpkg-reconfigure --frontend noninteractive locales  
  
RUN curl -sL https://asciinema.org/install | bash  
  
VOLUME ["/records"]  
  
ADD entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]

