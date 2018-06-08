FROM pipill/armhf-alpine  
RUN [ "cross-build-start" ]  
RUN apk add --no-cache perl  
RUN [ "cross-build-end" ]  
COPY cowsay /usr/local/bin/cowsay  
COPY docker.cow /usr/local/share/cows/default.cow  
ENTRYPOINT ["/usr/local/bin/cowsay"]  

