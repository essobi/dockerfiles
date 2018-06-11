# docker run -d \  
# -v /etc/localtime:/etc/localtime:ro \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY=$DISPLAY \  
# --name wireshark \  
# iaroki/wireshark  
FROM ubuntu:16.04  
MAINTAINER iaroki  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install -y \  
software-properties-common \  
\--no-install-recommends && \  
add-apt-repository ppa:wireshark-dev/stable && \  
apt-get update && \  
apt-get install -y \  
wireshark \  
&& rm -rf /var/lib/apt/lists/*  
ENV HOME /home/wireshark  
RUN useradd --create-home --home-dir $HOME wireshark \  
&& chown -R wireshark:wireshark $HOME  
RUN chown root:wireshark /usr/bin/dumpcap \  
&& setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap  
USER wireshark  
WORKDIR wireshark  
ENTRYPOINT [ "wireshark" ]  

