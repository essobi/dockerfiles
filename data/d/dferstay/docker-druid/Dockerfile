FROM ubuntu:16.04  
ARG DRUID_VERSION=0.12.0  
ARG TRANQUILITY_VERSION=0.8.2  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
curl \  
openjdk-8-jre \  
dnsutils \  
netcat  
  
RUN curl -L
http://static.druid.io/artifacts/releases/druid-${DRUID_VERSION}-bin.tar.gz |
tar -zxf - -C / && \  
mv /druid-${DRUID_VERSION} /druid  
RUN curl -o /druid/hadoop-dependencies/hadoop-client/2.7.3/hadoop-
aws-2.7.3.jar http://central.maven.org/maven2/org/apache/hadoop/hadoop-
aws/2.7.3/hadoop-aws-2.7.3.jar  
RUN curl -L http://static.druid.io/tranquility/releases/tranquility-
distribution-${TRANQUILITY_VERSION}.tgz | tar -zxf - -C / && \  
mv /tranquility-distribution-${TRANQUILITY_VERSION} /tranquility  
  
COPY run-druid.sh /druid/bin/  
COPY wait-for-dependencies.sh /druid/bin/  
  
# Add the druid user and group  
RUN adduser --system --group --no-create-home druid \  
&& chown -R druid:druid /druid \  
&& chown -R druid:druid /tranquility  
  
USER druid:druid  
  
# Expose ports:  
# 8081: HTTP (coordinator)  
# 8082: HTTP (broker)  
# 8083: HTTP (historical)  
# 8090: HTTP (overlord)  
# 8091: HTTP (middleManager)  
# 8100-8199: HTTP (middleManager workers (aka Peons))  
# 8200: HTTP (tranquility)  
EXPOSE 8081  
EXPOSE 8082  
EXPOSE 8083  
EXPOSE 8090  
EXPOSE 8091 8100-8199  
EXPOSE 8200  
WORKDIR /druid/  
  
CMD ["bin/run-druid.sh"]  

