FROM ubuntu:17.10  
MAINTAINER Herbert Shin  
  
ENV UID 1000  
ENV GID 1000  
USER root  
  
EXPOSE 9091 \  
51413/tcp \  
51413/udp \  
46882/udp \  
50052/udp  
  
ENV ULTIMATE_BLOCKLIST https://github.com/walshie4/Ultimate-Blocklist.git  
ENV BLOCKLIST_PATH /root/.config/transmission/blocklists  
  
# dependencies  
RUN apt-get update && \  
apt-get install -y \  
git \  
python \  
python-pip \  
transmission-cli  
  
# blocklists  
RUN mkdir -p ${BLOCKLIST_PATH} && \  
git clone ${ULTIMATE_BLOCKLIST} /tmp/Ultimate-Blocklist && \  
pip install -r /tmp/Ultimate-Blocklist/requirements.txt && \  
python /tmp/Ultimate-Blocklist/UltimateBlockList.py && \  
mv blocklist.txt ${BLOCKLIST_PATH}/$(date +%F).txt && \  
ln -sLf /torrents /root/Downloads && \  
rm -rf /tmp/Ultimate-Blocklist  
  
WORKDIR /torrents  
  
ENTRYPOINT ["/usr/bin/transmission-cli", "-b", "-D", "-er", "-m", "-t 0x28",
"-u 1", "-v"]  
# e1733c7d0321dd519f83c26333ceab9b -  

