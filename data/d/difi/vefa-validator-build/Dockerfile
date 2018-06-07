FROM java:8-jre  
MAINTAINER Erlend Klakegg Bergheim  
  
#RUN wget -q http://repo1.maven.org/maven2/no/difi/vefa/validator-
build/2.0.2/validator-build-2.0.2-jar-with-dependencies.jar -O /vefa-
validator-build.jar  
RUN wget -q https://jitpack.io/com/github/difi/vefa-validator/validator-
build/-SNAPSHOT/validator-build--SNAPSHOT-jar-with-dependencies.jar -O /vefa-
validator-build.jar  
  
VOLUME /src  
  
CMD java -jar /vefa-validator-build.jar -x -test /src  

