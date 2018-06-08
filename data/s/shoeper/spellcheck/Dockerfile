FROM debian:testing  
MAINTAINER Sven Höper <sven@hoeper.me>  
  
# https://stackoverflow.com/a/28406007/5923915  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
locale-gen  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# The last apt-get clean and rm -rf removes the temporary .deb packages  
# downloaded during the install process  
RUN apt-get update && \  
apt-get install --no-install-recommends -y \  
aspell \  
aspell-en \  
aspell-de \  
poppler-utils \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

