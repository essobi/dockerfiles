FROM openjdk:8u121-jre-alpine  
  
ENV SPARK_VERSION=2.1.0 SPARK_HOME=/opt/spark  
ENV PATH="${PATH}:$SPARK_HOME/bin"  
WORKDIR /opt  
  
RUN apk update && \  
apk add --no-cache curl bash && \  
curl -sSL http://d3kbcqa49mib13.cloudfront.net/spark-$SPARK_VERSION-bin-
hadoop2.7.tgz | tar xz && \  
find . -maxdepth 1 -type d -name "*spark*" -exec ln -sf {} $SPARK_HOME \; && \  
find . -type f \\( -name "*cmd" -o -name "*bat" \\) -delete && \  
apk del curl  
  
CMD ["spark-shell"]  

