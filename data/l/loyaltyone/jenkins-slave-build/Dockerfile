FROM loyaltyone/jenkins-slave:0.5.1  
  
#=========  
# SBT  
#=========  
  
ENV SBT_VERSION=1.1.0 \  
SBT_HOME=/usr/local/sbt  
ENV PATH=${PATH}:${SBT_HOME}/bin  
  
  
RUN curl -sL
"https://github.com/sbt/sbt/releases/download/v$SBT_VERSION/sbt-$SBT_VERSION.tgz"
| gunzip | tar -x -C /usr/local  
  
USER jenkins  
  
RUN sbt sbtVersion \  
&& rm -rf project  
  
USER root  
  
#================  
# MAVEN (3.3.9-3)  
#================  
  
ENV MAVEN_VERSION=3.3.9-3  
  
RUN apt-get update && apt-get install -y maven=$MAVEN_VERSION  
#================  
# Node  
#================  
  
COPY node-setup node-setup  
RUN chmod +x node-setup  
  
USER jenkins  
# Install more node versions using NVM (already installed) as well as packages  
RUN ./node-setup && rm node-setup  
  
USER root  
  
#================  
# Scala  
#================  
COPY fetch-cache-scala /usr/local/bin/fetch-cache-scala  
RUN chmod +x /usr/local/bin/fetch-cache-scala  
  
ENTRYPOINT ["/usr/local/bin/entry-point", "/usr/local/bin/fetch-cache-scala",
"/usr/local/bin/jenkins-slave"]  
  
USER root  
RUN rm -rf /home/jenkins/build  

