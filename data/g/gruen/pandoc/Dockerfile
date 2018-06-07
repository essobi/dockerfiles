FROM ubuntu:16.04  
LABEL maintainer "Darren Green <darren@gruen.site>"  
  
RUN apt-get update -y \  
&& apt-get install -y \  
pandoc \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean \  
&& apt-get autoremove -y  
  
WORKDIR /root/pandoc  
  
ENTRYPOINT ["pandoc"]  

