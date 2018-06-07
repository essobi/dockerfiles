FROM openjdk:8-jre-slim  
  
MAINTAINER Thomas Goureau <thomas.goureau@gmail.com>  
  
ENV VERSION 4.0  
ENV NGRAMS_V 20150913  
ADD https://www.languagetool.org/download/LanguageTool-$VERSION.zip
/LanguageTool-$VERSION.zip  
ADD https://www.languagetool.org/download/ngram-data/ngrams-fr-$NGRAMS_V.zip
/ngrams-fr-$NGRAMS_V.zip  
  
# add config file  
ADD server.properties /server.properties  
  
RUN unzip LanguageTool-$VERSION.zip \  
&& rm LanguageTool-$VERSION.zip \  
&& mkdir /ngrams-fr-$NGRAMS_V \  
&& unzip ngrams-fr-$NGRAMS_V.zip -d /ngrams-fr-$NGRAMS_V \  
&& rm ngrams-fr-$NGRAMS_V.zip  
  
WORKDIR /LanguageTool-$VERSION  
  
CMD ["java", "-cp", "languagetool-server.jar",
"org.languagetool.server.HTTPServer","--config", "/server.properties", "--
port", "8010", "--public", "--allow-origin", "\"*\""]  
EXPOSE 8010  

