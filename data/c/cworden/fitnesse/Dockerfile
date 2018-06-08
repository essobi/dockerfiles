FROM java:latest  
MAINTAINER Cody Worden <cjworden@greatergood.com>  
  
ENV FITNESSE_RELEASE 20161106  
RUN mkdir /FitNesse \  
&& curl -fsSL -o fitnesse-standalone.jar "http://www.fitnesse.org/fitnesse-
standalone.jar?responder=releaseDownload&release=$FITNESSE_RELEASE"  
  
VOLUME /FitNesse  
EXPOSE 80  
CMD java -Xmx256m -jar fitnesse-standalone.jar

