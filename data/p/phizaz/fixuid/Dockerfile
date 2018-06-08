FROM ubuntu:16.04  
  
########################################  
# ROOT MODE  
########################################  
  
###### SETUP APT-FAST #####################  
RUN apt-get update && apt-get install -y aria2 git \  
&& git clone https://github.com/ilikenwf/apt-fast /tmp/apt-fast \  
&& cp /tmp/apt-fast/apt-fast /usr/bin \  
&& chmod +x /usr/bin/apt-fast \  
&& cp /tmp/apt-fast/apt-fast.conf /etc  
  
###### SETUP CURL #########################  
RUN apt-fast update && apt-fast install -y curl  
  
###### SETUP FIXUID #######################  
RUN addgroup --gid 1000 docker && \  
adduser --uid 1000 \--ingroup docker --home /home/docker --shell /bin/sh
--disabled-password --gecos "" docker  
  
RUN USER=docker && \  
GROUP=docker && \  
curl -SsL
https://github.com/boxboat/fixuid/releases/download/v0.1/fixuid-0.1-linux-
amd64.tar.gz | tar -C /usr/local/bin -xzf - && \  
chown root:root /usr/local/bin/fixuid && \  
chmod 4755 /usr/local/bin/fixuid && \  
mkdir -p /etc/fixuid && \  
printf "user: $USER\ngroup: $GROUP\n" > /etc/fixuid/config.yml  
  
ENTRYPOINT ["fixuid"]  

