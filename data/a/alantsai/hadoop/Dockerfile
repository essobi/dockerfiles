FROM openjdk:8-jdk-slim  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Testing and Evaluating Hadoop with .net core 2.0 sdk
installed" \  
org.label-schema.description="Easy evaluate hadoop with running .net core
console as map reduce job" \  
org.label-
schema.url="https://github.com/alantsai/dockerfiles/tree/master/src/hadoop" \  
org.label-schema.vcs-url="https://github.com/alantsai/dockerfiles.git" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.version="v-hadoop-2.7.2-dotnetcore2.0-stretch_slim" \  
org.label-schema.vendor="Alan Tsai" \  
org.label-schema.docker.cmd="docker-compose -d" \  
org.label-schema.schema-version="1.0.0-rc1"  
  
# Hadoop  
ENV HADOOP_VERSION 2.7.2  
ENV HADOOP_HOME /usr/local/hadoop  
ENV HADOOP_OPTS -Djava.library.path=/usr/local/hadoop/lib/native  
ENV PATH $PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
wget \  
&& wget
http://archive.apache.org/dist/hadoop/core/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz
\  
&& apt-get remove -y wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& tar -zxf /hadoop-$HADOOP_VERSION.tar.gz \  
&& rm /hadoop-$HADOOP_VERSION.tar.gz \  
&& mv hadoop-$HADOOP_VERSION /usr/local/hadoop \  
&& mkdir -p /usr/local/hadoop/logs  
  
# .NET Core  
#RUN apt-get update && \  
# DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
# curl libunwind8 gettext apt-transport-https gnupg \  
# && curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >
microsoft.gpg \  
# && mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg \  
# && sh -c 'echo "deb [arch=amd64]
https://packages.microsoft.com/repos/microsoft-debian-stretch-prod stretch
main" > #/etc/apt/sources.list.d/dotnetdev.list' \  
# && apt-get update \  
# && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
dotnet-sdk-2.0.0 \  
# && apt-get remove --purge -y curl libunwind8 apt-transport-https gnupg \  
# && rm /etc/apt/trusted.gpg.d/microsoft.gpg \  
# && rm -rf /var/lib/apt/lists/*  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libc6 \  
libcurl3 \  
libgcc1 \  
libgssapi-krb5-2 \  
libicu57 \  
liblttng-ust0 \  
libssl1.0.2 \  
libstdc++6 \  
libunwind8 \  
libuuid1 \  
zlib1g \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV DOTNET_SDK_VERSION 2.1.3  
ENV DOTNET_SDK_DOWNLOAD_URL
https://dotnetcli.blob.core.windows.net/dotnet/Sdk/$DOTNET_SDK_VERSION/dotnet-
sdk-$DOTNET_SDK_VERSION-linux-x64.tar.gz  
ENV DOTNET_SDK_DOWNLOAD_SHA
509b88895fd5a6a90e245141eb52f188aa9ee7d20188c213892483c142900d6975013aef9ca6d8da986cc5617a2c3571e22318297c51578b871c047602757600  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -SL $DOTNET_SDK_DOWNLOAD_URL --output dotnet.tar.gz \  
&& echo "$DOTNET_SDK_DOWNLOAD_SHA dotnet.tar.gz" | sha512sum -c - \  
&& mkdir -p /usr/share/dotnet \  
&& tar -zxf dotnet.tar.gz -C /usr/share/dotnet \  
&& rm dotnet.tar.gz \  
&& ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet \  
&& apt-get remove --purge -y curl  
  
# add Hadoop config  
COPY conf $HADOOP_HOME/etc/hadoop/  
  
ENV JAVA_HOME /usr  
  
# format HDFS  
RUN mkdir -p /hdfs/data /hdfs/name /hdfs/secondary \  
&& hdfs namenode -format  
  
VOLUME /hdfs  
  
# script for node startup  
ADD start-hadoop.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/start-hadoop.sh \  
&& chmod +x /usr/local/hadoop/etc/hadoop/hadoop-env.sh  
  
# HDFS ports  
EXPOSE 50010 50020 50070 50075 50090 8020 9000 9001  
# MapReduce UI  
EXPOSE 19888  
# YARN ports  
EXPOSE 8025 8030 8031 8032 8033 8040 8042 8088  
ENTRYPOINT ["/usr/local/bin/start-hadoop.sh"]

