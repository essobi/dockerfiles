FROM java:openjdk-8-jre-alpine  
  
ENV VERSION 3.7  
ADD https://www.languagetool.org/download/LanguageTool-$VERSION.zip
/LanguageTool-$VERSION.zip  
  
RUN apk --update add unzip \  
&& unzip LanguageTool-$VERSION.zip \  
&& rm LanguageTool-$VERSION.zip  
  
WORKDIR /LanguageTool-$VERSION  
  
CMD ["java", "-cp", "languagetool-server.jar",
"org.languagetool.server.HTTPServer", "--port", "8010", "--public" ]  
EXPOSE 8010  

