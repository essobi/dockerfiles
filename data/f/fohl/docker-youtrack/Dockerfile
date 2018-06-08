FROM ubuntu:14.04.2  
  
MAINTAINER Mischa Holz  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV JAVA_HOME /opt/jdk/jre  
ENV PATH $PATH:/opt/jdk/jre/bin  
  
RUN apt-get update && apt-get install -y wget  
  
RUN wget --no-check-certificate -O /tmp/pkg.tar.gz --header "Cookie:
oraclelicense=a" http://download.oracle.com/otn-
pub/java/jdk/7u65-b17/jdk-7u65-linux-x64.tar.gz && \  
tar -zxf /tmp/pkg.tar.gz --xform='s/[^\/]*/jdk/' -C /opt && \  
rm -rf /tmp/*  
  
ENV YOUTRACK_VERSION 6.0.12634  
RUN wget http://download.jetbrains.com/charisma/youtrack-$YOUTRACK_VERSION.jar
-O youtrack.jar  
  
# RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 80  
CMD \  
java \  
-Xmx1g \  
-Dorg.tanukisoftware.wrapper.WrapperSimpleApp.waitForStartMain=true \  
-Dorg.tanukisoftware.wrapper.WrapperSimpleApp.maxStartMainWait=300 \  
-XX:MaxPermSize=128m \  
-XX:+HeapDumpOnOutOfMemoryError \  
-XX:+UseConcMarkSweepGC \  
-XX:+DisableExplicitGC \  
-XX:SoftRefLRUPolicyMSPerMB=10000 \  
-XX:+UseBiasedLocking \  
-Djava.awt.headless=true \  
-Xss4m \  
-Dcatalina.base=/home/youtrack/standalone \  
-Djetbrains.dnq.cachePercent=25 \  
-Djetbrains.dnq.sharedCache=false \  
-Djetbains.webr.uiQueryCancellingPolicyTimeout=80000 \  
-Djetbrains.dnq.fairLatches=false \  
-Djetbrains.dnq.readUncommittedForCachingThread=true \  
-Djetbrains.youtrack.disableBrowser=true \  
-jar youtrack.jar 80  

