FROM java:8-alpine  
  
ARG MINECRAFT_VERSION=1.12  
ARG PAPER_BUILD=1179  
ARG
PAPER_URL=https://ci.destroystokyo.com/job/PaperSpigot/${PAPER_BUILD}/artifact/paperclip-${PAPER_BUILD}.jar  
ARG
PAPER_SHA512=85d74e5ae9ed60d00965b8e183409c94c1d139f61e77fa6f8ff0a0cd89a6347b96cb565c97a7e36fb20c588a831a9fe5892914e0988bde9d7e69dfaded5fe6b3  
  
WORKDIR /data  
ADD "${PAPER_URL}" /srv/paper.jar  
RUN cd /srv &&\  
java -jar paper.jar --version &&\  
mv cache/patched*.jar paper.jar &&\  
rm -rf cache &&\  
chmod 444 /srv/paper.jar  
  
ADD start.sh /usr/local/bin/paper  
RUN chmod +x /usr/local/bin/paper  
  
ENV JAVA_ARGS "-Xmx1G"  
ENV SPIGOT_ARGS ""  
ENV PAPER_ARGS ""  
VOLUME "/data"  
  
CMD ["paper"]  

