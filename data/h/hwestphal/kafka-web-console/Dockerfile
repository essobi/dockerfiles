FROM dockerfile/java:oracle-java7  
MAINTAINER Harald Westphal <h.westphal@gmx.de>  
  
RUN \  
cd / && \  
wget -q http://downloads.typesafe.com/play/2.2.1/play-2.2.1.zip && \  
unzip play-2.2.1.zip && \  
rm -f play-2.2.1.zip && \  
git clone https://github.com/claudemamo/kafka-web-console.git && \  
cd /kafka-web-console && \  
git checkout tags/v2.0.0 && \  
/play-2.2.1/play clean compile stage  
  
EXPOSE 9000  
CMD exec /kafka-web-console/target/universal/stage/bin/kafka-web-console
-Duser.dir=/data -DapplyEvolutions.default=true  

