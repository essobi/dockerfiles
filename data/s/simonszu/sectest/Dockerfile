  
FROM debian:latest  
  
RUN apt-get update \  
&& apt-get install -y \  
telnet \  
nmap \  
ssh \  
netcat \  
traceroute \  
mtr \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN useradd -ms /bin/bash executor  
USER executor  
WORKDIR /home/executor  
  
ENTRYPOINT ["tail", "-f", "/dev/null"]  

