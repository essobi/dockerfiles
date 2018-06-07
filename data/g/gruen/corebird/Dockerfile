FROM ubuntu:16.04  
LABEL maintainer "Darren Green <darren@gruen.site>"  
CMD ["corebird"]  
WORKDIR /root  
RUN apt-get update \  
&& apt-get install -y \  
software-properties-common \  
&& add-apt-repository ppa:ubuntuhandbook1/corebird \  
&& apt-get update \  
&& apt-get install -y \  
corebird \  
&& apt-get clean \  
&& apt-get purge -y \  
software-properties-common \  
&& rm -rf /var/lib/apt/lists/*  
  

