FROM openjdk:8-jre-alpine  
  
ENV LT_VERSION 4.1  
RUN apk update && \  
apk add \  
curl unzip && \  
cd /srv && \  
curl -o LanguageTool-$LT_VERSION.zip
https://www.languagetool.org/download/LanguageTool-$LT_VERSION.zip && \  
unzip LanguageTool-$LT_VERSION.zip && \  
rm LanguageTool-$LT_VERSION.zip && \  
rm -rf /var/cache/apk/*  
  
EXPOSE 8081  
WORKDIR /srv/LanguageTool-$LT_VERSION  
  
CMD java -cp languagetool-server.jar org.languagetool.server.HTTPServer
--public --port 8081  

