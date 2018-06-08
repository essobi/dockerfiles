FROM alpine:3.7 as gh-deps  
  
ENV PT_VERSION 2.0.2  
  
WORKDIR /tmp  
  
RUN \  
PROJECT_URL="https://github.com/taniman/profit-trailer" && \  
ARTIFACT_URL="$PROJECT_URL/releases/download/v$PT_VERSION/ProfitTrailer.zip"
&& \  
wget -O ProfitTrailer.zip $ARTIFACT_URL && \  
unzip ProfitTrailer.zip && \  
(cd ProfitTrailer; rm pm2-ProfitTrailer.json Run-ProfitTrailer.cmd) && \  
mv ProfitTrailer /  
  
  
  
FROM openjdk:8-jre-alpine  
  
ENV PT_VERSION $PT_VERSION  
  
COPY \--from=gh-deps /ProfitTrailer /ProfitTrailer  
COPY ./bin /usr/local/bin  
COPY ./lib /usr/local/lib/pt  
  
RUN mkdir -p /appdata/config /appdata/data /appdata/logs  
  
RUN \  
addgroup -g 1000 pt && \  
adduser -D -s /bin/sh -G pt -u 1000 ptuser  
  
RUN chown -R ptuser:pt /ProfitTrailer /appdata  
  
VOLUME /appdata/config  
VOLUME /appdata/data  
VOLUME /appdata/logs  
  
EXPOSE 8081  
  
USER ptuser  
WORKDIR /config  
  
CMD [ "startup" ]  

