FROM freckleiot/docker-jenkins-slave:1.0  
#==============  
# SBT (v1.1.4)  
#==============  
ENV SBT_VERSION=1.1.4  
ENV SBT_HOME=/usr/local/sbt  
ENV PATH=${PATH}:${SBT_HOME}/bin  
  
RUN curl -sL
"https://github.com/sbt/sbt/releases/download/v$SBT_VERSION/sbt-$SBT_VERSION.tgz"
| gunzip | tar -x -C /usr/local  
  
USER jenkins  
  
RUN sbt sbtVersion \  
&& rm -rf project  
  
USER root  
  
#================  
# Maven (3.3.9-3)  
#================  
ENV MAVEN_VERSION=3.3.9-3  
RUN apt-get update && apt-get install -y maven=$MAVEN_VERSION  
  
#==========================  
# Leiningen (Latest Stable)  
#==========================  
ENV LEIN_ROOT=true  
RUN wget -q -O /usr/bin/lein \  
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein \  
&& chmod +x /usr/bin/lein  
  
USER jenkins  
  
RUN lein  
  
USER root  
  
#==========================  
# Scala Ammonite REPL + Shell for scripting  
#==========================  
# predef.sc to make REPL a usable system shell  
RUN mkdir -p ~/.ammonite && curl -L -o ~/.ammonite/predef.sc
https://git.io/vHaKQ  
  
# download Ammonite (accessible via `amm`)  
RUN curl -L -o /usr/local/bin/amm
https://github.com/lihaoyi/Ammonite/releases/download/1.1.0/2.12-1.1.0 && \  
chmod +x /usr/local/bin/amm  
  
COPY initialize-amm.sc example.sc  
  
USER jenkins  
  
RUN amm example.sc && rm example.sc  
  
USER root  
  
#=============  
# Fetch caches  
#=============  
COPY fetch-cache /usr/local/bin/fetch-cache  
RUN chmod +x /usr/local/bin/fetch-cache  
  
ENTRYPOINT ["/usr/local/bin/entry-point", "/usr/local/bin/fetch-cache",
"/usr/local/bin/jenkins-slave"]  
  
USER root  
RUN rm -rf /home/jenkins/build  

