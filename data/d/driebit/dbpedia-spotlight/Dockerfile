FROM openjdk:8-jre-alpine  
  
ENV VERSION=latest  
ENV MEMORY=2g  
ENV LANGUAGE=en  
ENV LANGUAGE_MODEL=${LANGUAGE}.tar.gz  
  
ADD http://spotlight.sztaki.hu/downloads/dbpedia-spotlight-${VERSION}.jar /  
ADD http://spotlight.sztaki.hu/downloads/latest_models/$LANGUAGE_MODEL /  
  
CMD java -Xmx${MEMORY} -jar /dbpedia-spotlight-${VERSION}.jar /${LANGUAGE}
http://localhost:80/rest/  
  
EXPOSE 80  

