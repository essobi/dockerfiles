FROM kong:0.11  
ENV NILDNS_VERSION v0.0.5  
RUN wget -q -O /nildns
https://github.com/tumf/nildns/releases/download/${NILDNS_VERSION}/nildns_linux_amd64
&&\  
chmod +x /nildns  
COPY kong.conf /  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
CMD ["kong", "start","--conf","/kong.conf"]  

