# TiddlyWiki over NodeJS on Alpine Linux  
#  
# VERSION 0.3  
#  
FROM alpine:3.7  
EXPOSE 8086  
ENV WIKI_HOME=/wiki  
RUN apk add --update nodejs iproute2 \  
&& npm install -g tiddlywiki \  
&& tiddlywiki --version  
COPY ./start.sh ${WIKI_HOME}/start.sh  
RUN addgroup wiki && adduser -G wiki -h ${WIKI_HOME} -D wiki \  
&& chmod +x ${WIKI_HOME}/start.sh  
USER wiki  
WORKDIR ${WIKI_HOME}  
ENTRYPOINT ["./start.sh"]  
VOLUME ["${WIKI_HOME}"]  

