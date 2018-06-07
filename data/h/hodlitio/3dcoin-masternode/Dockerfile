FROM hodlitio/3dcoin-builder:v0.13.3.2  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="HODLit 3DCoin Masternode" \  
org.label-schema.description="Masternode for 3DCoin" \  
org.label-schema.url="hodlit.io" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/HODLit-3dcoin/3dcoin-masternode"
\  
org.label-schema.vendor="Varts" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
RUN /usr/sbin/useradd -s /bin/bash -m -d /home/crypto crypto \  
&& chown crypto:crypto -R /home/crypto  
  
USER crypto  
  
RUN mkdir -p /home/crypto/.3dcoin \  
&& cd /home/crypto/.3dcoin \  
&& echo "rpcuser=RPC_USER_REPLACE_AT_RUNTIME" > 3dcoin.conf \  
&& echo "rpcpassword=RPC_PASSWORD_REPLACE_AT_RUNTIME" >> 3dcoin.conf \  
&& echo "rpcallowip=127.0.0.1" >> 3dcoin.conf \  
&& echo "server=1" >> 3dcoin.conf \  
&& echo "daemon=1" >> 3dcoin.conf \  
&& echo "listen=1" >> 3dcoin.conf \  
&& echo "listen=64" >> 3dcoin.conf \  
&& echo "externalip=MN_IP_REPLACE_AT_RUNTIME" >> 3dcoin.conf \  
&& echo "masternode=1" >> 3dcoin.conf \  
&& echo "masternodeprivkey=MN_PK_REPLACE_AT_RUNTIME" >> 3dcoin.conf \  
&& echo "#!/bin/bash" > entrypoint.sh \  
&& echo "" >> entrypoint.sh \  
&& echo "if [ \"\$#\" -ne 2 ]; then echo 'You need to supply 2 parameters.
PARAM1: masternode external ip, PARAM2: masternode private key' && exit; fi"
>> entrypoint.sh \  
&& echo "sed -i -- 's/RPC_USER_REPLACE_AT_RUNTIME/$(echo
\"$(whoami)-$(date)-$(hostname)-$(ip addr show)-$(df -h)-$(ps -ef)\" | md5sum
| cut -d" " -f 1)/g' ./3dcoin.conf && sleep 1 && sed -i --
's/RPC_PASSWORD_REPLACE_AT_RUNTIME/$(echo \"$(whoami)-$(date)-$(hostname)-$(ip
addr show)-$(df -h)-$(ps -ef)\" | md5sum | cut -d" " -f 1)/g' ./3dcoin.conf &&
sed -i -- \"s/MN_IP_REPLACE_AT_RUNTIME/\$1/g\" ./3dcoin.conf && sed -i --
\"s/MN_PK_REPLACE_AT_RUNTIME/\$2/g\" ./3dcoin.conf && 3dcoind && sleep 5 &&
while true; do echo \"\$(3dcoin-cli mnsync status)\" && sleep 3 && if [ -n
\"\$(3dcoin-cli mnsync status | grep MASTERNODE_SYNC_FINISHED)\" ]; then
break; fi done && 3dcoin-cli masternode start && while true; do echo
\"\$(3dcoin-cli masternode status)\" && sleep 600; done" >> entrypoint.sh \  
&& chmod a+x ./entrypoint.sh  
  
WORKDIR /home/crypto/.3dcoin  
ENTRYPOINT ["/home/crypto/.3dcoin/entrypoint.sh"]  

