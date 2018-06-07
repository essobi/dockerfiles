FROM java:8  
MAINTAINER Simeon H.K. Fitch <fitch@datamininglab.com>  
  
# SBT Version  
ENV SBT_VERSION 0.13.7  
ENV SBT_HOME /usr/local/sbt  
  
ENV SBT_BUNDLE https://dl.bintray.com/sbt/native-
packages/sbt/${SBT_VERSION}/sbt-${SBT_VERSION}.tgz  
  
RUN curl -L -s ${SBT_BUNDLE} | tar -xz -C /usr/local/  
RUN cd /usr/local/bin && ln -s ${SBT_HOME}/bin/sbt  
  
RUN adduser --disabled-password --gecos '' sbt  
USER sbt  
WORKDIR /home/sbt  
  
RUN mkdir -p /home/sbt/.sbt/0.13/plugins  
COPY files/plugins/*.sbt /home/sbt/.sbt/0.13/plugins/  
COPY files/global.sbt /home/sbt/.sbt/0.13/  
  
# We run the `about` task to get baseline dependencies downloaded.  
RUN sbt about  
  
# By default just run the shell  
CMD ["/usr/local/bin/sbt"]  
  

