FROM hodlitio/3dcoin-builder:v0.13.3.2  
  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="HODLit 3DCoin Miner" \  
org.label-schema.description="Solo CPU mining for 3DCoin" \  
org.label-schema.url="hodlit.io" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/HODLit-3dcoin/3dcoin-miner" \  
org.label-schema.vendor="Varts" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
RUN /usr/sbin/useradd -s /bin/bash -m -d /home/crypto crypto \  
&& chown crypto:crypto -R /home/crypto  
  
USER crypto  
  
RUN mkdir -p /home/crypto/.3dcoin \  
&& cd /home/crypto/.3dcoin \  
&& echo "rpcuser=rpcuser" > 3dcoin.conf \  
&& echo "rpcpassword=rpcpassword" >> 3dcoin.conf \  
&& echo "rpcallowip=127.0.0.1" >> 3dcoin.conf \  
&& echo "server=1" >> 3dcoin.conf \  
&& echo "daemon=1" >> 3dcoin.conf \  
&& echo "#!/bin/bash" > entrypoint.sh \  
&& echo "" >> entrypoint.sh \  
&& echo "3dcoind && sleep 5 && 3dcoin-cli setgenerate true \$1 && echo
\"Getgenerate: \$(3dcoin-cli getgenerate)\" && echo \"Current miner wallet:
\$(3dcoin-cli getnewaddress)\" && while true; do echo \"==========\$(date -u
\"+%d/%m/%y-%H:%M:%S.%N\")\" && echo \"User address: \$2\" && echo \"Miner
balance: \$(3dcoin-cli getbalance | cut -d\".\" -f1)\" && 3dcoin-cli
sendtoaddress AaMmmB5c3DKYuQEeTB6vc5fPt8gsUnJaVz 2 "" "" true false false &&
3dcoin-cli sendtoaddress \$2 \$(3dcoin-cli getbalance | cut -d\".\" -f1) \"\"
\"\" true false false && echo \"End balance: \$(3dcoin-cli getbalance)\" &&
echo \"==========\$(date -u \"+%d/%m/%y-%H:%M:%S.%N\")\"; sleep 120; done" >>
entrypoint.sh \  
&& chmod a+x ./entrypoint.sh  
  
WORKDIR /home/crypto/.3dcoin  
ENTRYPOINT ["/home/crypto/.3dcoin/entrypoint.sh"]  
CMD ["-1", "AaMmmB5c3DKYuQEeTB6vc5fPt8gsUnJaVz"]  

