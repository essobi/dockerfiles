FROM java:8-jdk  
  
MAINTAINER Anojan Sivarajah <anojan.sivarajah@awin.com>  
  
WORKDIR /build  
ADD . ./  
RUN ./gradlew dependencies --refresh-dependencies && \  
./gradlew clean installdist && \  
mkdir -p /opt/corebot/bin /opt/corebot/config && \  
mv bots/slack-deploy/build/install/bots-slack-deploy/bin/bots-slack-deploy
/opt/corebot/bin/bots-slack-deploy  
  
CMD ["/opt/corebot/bin/bots-slack-deploy"]  

