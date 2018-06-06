FROM frolvlad/alpine-glibc:alpine-3.4  
LABEL vendor=makeomatic \  
version_tags="[\"0.4\",\"0.4.1\"]"  
  
ENV NOMAD_VERSION=0.4.1 \  
NOMAD_SHA256=0cdb5dd95c918c6237dddeafe2e9d2049558fea79ed43eacdfcd247d5b093d67  
  
RUN apk --no-cache --update add curl  
  
RUN curl -sSL -o /tmp/nomad.zip
https://releases.hashicorp.com/nomad/${NOMAD_VERSION}/nomad_${NOMAD_VERSION}_linux_amd64.zip
&& \  
echo "${NOMAD_SHA256} /tmp/nomad.zip" | sha256sum -c - && unzip /tmp/nomad.zip
-d /usr/local/bin && \  
rm -rf /tmp/*  
  
VOLUME ["/data", "/config"]  
  
# http server (client+server): 4646  
# rpc (server raft): 4647  
# serf (server gossip): 4648  
EXPOSE 4646 4647 4648  
ADD entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  

