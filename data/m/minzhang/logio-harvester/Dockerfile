FROM mhart/alpine-node:latest  
  
RUN apk add --update python make gcc g++ && rm -rf /var/cache/apk/* \  
&& adduser -s /bin/false -g "" -D logio \  
&& export USER=logio && export HOME=/home/logio \  
&& npm install -g log.io --user "logio" \  
&& apk del make gcc g++ python  
  
EXPOSE 28778  
USER logio  
ENV HOME /home/logio  
ENV USER logio  
WORKDIR /home/logio  
  
CMD ["log.io-harvester"]  

