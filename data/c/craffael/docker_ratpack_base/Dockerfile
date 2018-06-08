FROM java:8  
MAINTAINER Raffael Casagrande <raffael@casagrande.ch>  
  
# Use dumb-init to run the processes:  
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64  
RUN chmod +x /usr/local/bin/dumb-init  
  
# use bash shell  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
# install zip:  
RUN apt-get update && apt-get install zip  
# install docker:  
RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-1.13.1.tgz
&& tar --strip-components=1 -xvzf docker-1.13.1.tgz -C /usr/local/bin  
  
# download sdkman  
RUN curl -s get.sdkman.io | bash # install sdkman  
  
RUN source "/root/.sdkman/bin/sdkman-init.sh" \  
&& sdk install groovy 2.4.6 < /dev/null \  
&& sdk install gradle 2.12 < /dev/null  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/dumb-init", "/entrypoint.sh"]  
  
# Set /opt/ as working directory  
WORKDIR /opt/  
  
# Default command: run gradle in the current working directory  
#CMD source ~/.bashrc && gradle run  

