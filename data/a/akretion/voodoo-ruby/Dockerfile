FROM ruby:2.4  
RUN mkdir -p /workspace &&\  
adduser ubuntu  
WORKDIR /workspace  
  
# Install node required by locomotive and many project  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y nodejs vim && \  
apt-get clean && \  
ln -sf /usr/bin/nodejs /usr/bin/node  
  
# grab gosu for easy step-down from root  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.10/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.10/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
COPY stack/entrypoint /usr/local/bin/entrypoint  
COPY stack/bash_aliases /home/ubuntu/.bash_aliases  
  
ENV LANG C.UTF-8  
ENTRYPOINT ["/usr/local/bin/entrypoint"]  
EXPOSE 3000  
EXPOSE 3333  

