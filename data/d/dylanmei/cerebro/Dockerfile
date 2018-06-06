FROM openjdk:8-slim  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y curl ca-certificates git
\  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# SBT  
ENV SBT_VERSION "0.13.5"  
ENV SBT_HOME /usr/sbt  
ENV PATH $PATH:$SBT_HOME/bin  
  
RUN curl -sL --retry 3 "http://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" \  
| gunzip \  
| tar -x -C /usr/  
  
EXPOSE 9000  
WORKDIR /usr/cerebro  
  
# CEREBRO  
RUN git clone https://github.com/lmenezes/cerebro /usr/src/cerebro \  
&& cd /usr/src/cerebro \  
&& git checkout master \  
&& sbt stage \  
&& cp -r target/universal/stage/* /usr/cerebro/ \  
&& rm -rf /usr/src/cerebro /root/.ivy2  
  
CMD ["bin/cerebro", "-Dhosts.0.host=http://localhost:9200"]  

