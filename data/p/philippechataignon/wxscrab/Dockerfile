FROM alpine:3.5  
  
RUN apk --update add python py-twisted py-pip  
RUN adduser -u 50000 -D -H scrabble  
COPY gen /  
RUN tar xf dico-1.02.linux-x86_64.tar.gz  
COPY dic/ods7.dawg /dic/  
COPY server /server/  
RUN chown scrabble /server/log /server/partie  
USER scrabble  
EXPOSE 12345  
WORKDIR /server  
CMD ./go_server  

