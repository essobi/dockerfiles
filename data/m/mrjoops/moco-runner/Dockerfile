FROM openjdk:jre-alpine  
  
ADD http://central.maven.org/maven2/com/github/dreamhead/moco-
runner/0.11.1/moco-runner-0.11.1-standalone.jar ./moco-runner-standalone.jar  
  
EXPOSE 80  
ENTRYPOINT java -jar moco-runner-standalone.jar http -p 80 -c $MOCO_JSON  

