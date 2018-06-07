FROM busybox:ubuntu-14.04  
WORKDIR /bin  
RUN wget http://stedolan.github.io/jq/download/linux64/jq && \  
chmod +x jq  
ENTRYPOINT ["/bin/jq"]  

