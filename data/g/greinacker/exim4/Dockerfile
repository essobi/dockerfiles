FROM ubuntu:16.04  
RUN apt-get update -qq \  
&& apt-get upgrade -y \  
&& apt-get install -y exim4-daemon-light mailutils xtail \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD start.sh /exim_start  
RUN chmod +x /exim_start  
  
ENV EXIM_LOCALINTERFACE=0.0.0.0  
ENTRYPOINT ["/exim_start"]  

