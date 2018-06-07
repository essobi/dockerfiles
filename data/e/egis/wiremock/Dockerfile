FROM egis/base  
WORKDIR /wiremock  
ADD run.sh .  
RUN ansible-role ansiblebit.oracle-java -c local  
ARG VERSION  
ARG PORT  
ENV VERSION ${VERSION:-2.8.0}  
ENV PORT ${PORT:-9999}  
  
  
ADD http://repo1.maven.org/maven2/com/github/tomakehurst/wiremock-
standalone/$VERSION/wiremock-standalone-$VERSION.jar /wiremock/wiremock.jar  
  
ENV TERM xterm  
EXPOSE $PORT  
CMD ["/bin/bash", "run.sh"]

