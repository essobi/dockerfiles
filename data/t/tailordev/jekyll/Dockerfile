FROM mwallasch/docker-ruby-node  
MAINTAINER TailorDev <hello@tailordev.fr>  
  
RUN apt-get update && apt-get install -y locales && rm -rf
/var/lib/apt/lists/*  
RUN echo "en_US UTF-8" > /etc/locale.gen  
RUN locale-gen en_US.UTF-8  
  
ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8  

