FROM openjdk:jre-alpine  
MAINTAINER Leonid Boykov <boykov@iias.spb.su>  
  
ENV RELEASE_SERVER=spotlight.sztaki.hu \  
RELEASE_FILENAME=dbpedia-spotlight-latest.jar \  
LANGUAGE=en \  
MEMORY=8G  
  
# download dbpedia spotlight files  
RUN wget -q http://$RELEASE_SERVER/downloads/$RELEASE_FILENAME \  
&& wget -q -O -
http://$RELEASE_SERVER/downloads/latest_models/$LANGUAGE.tar.gz | tar xzf - -C
"/"  
  
EXPOSE 80/tcp  
  
CMD java -Dfile.encoding=UTF-8 -Xmx${MEMORY} -jar /dbpedia-spotlight-
latest.jar /${LANGUAGE} http://localhost/rest  

