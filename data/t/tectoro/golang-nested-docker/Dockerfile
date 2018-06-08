FROM golang:1.6  
#Install docker and util  
RUN apt-get update \  
&& apt-get install -y bsdmainutils \  
&& curl -sSL https://get.docker.com/ | sh \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/*  

