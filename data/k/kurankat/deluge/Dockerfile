FROM ubuntu:xenial  
  
ARG BUILD_DATE  
ARG VERSION  
LABEL maintainer="github/kurankat"  
  
ENV HOME /home/user  
  
RUN groupadd -g 1000 user \  
&& useradd -r -u 1000 -g 1000 --create-home --home-dir $HOME user  
  
RUN apt update && apt -y install software-properties-common curl \  
&& add-apt-repository ppa:deluge-team/ppa \  
&& apt update \  
&& apt -y install deluged deluge-web deluge-console  
  
COPY entrypoint.sh /  
  
RUN chmod +x /entrypoint.sh  
  
EXPOSE 8112 58846 58946 58946/udp  
VOLUME /home/user/.config/deluge /downloads /watch  
  
RUN chown -R user:user $HOME && \  
chown -R user:user /downloads && \  
chown -R user:user /watch && \  
chown user:user /entrypoint.sh  
  
USER user  
WORKDIR $HOME  
  
ENTRYPOINT ["/entrypoint.sh"]  

