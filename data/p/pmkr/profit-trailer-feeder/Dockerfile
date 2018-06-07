FROM debian:stretch as gh-deps  
  
ENV FEEDER_VERSION 1.4.0.459  
RUN apt-get update && apt-get install -y wget unzip  
  
WORKDIR /tmp  
  
RUN \  
PROJECT_URL="https://github.com/mehtadone/PTFeeder" && \  
ARTIFACT_URL="$PROJECT_URL/releases/download/pt-feeder-v$FEEDER_VERSION/pt-
feeder-v$FEEDER_VERSION.zip" && \  
wget -O feeder.zip $ARTIFACT_URL && \  
mkdir feeder && \  
unzip -d feeder feeder.zip && \  
chmod +x feeder/pt-feeder.dll && \  
mv feeder /usr/local/lib/feeder  
  
FROM microsoft/dotnet:2.0.5-runtime-stretch as dotnet  
#FROM microsoft/dotnet-nightly:2.1-runtime-alpine as dotnet  
ENV FEEDER_VERSION 1.4.0.459  
COPY \--from=gh-deps /usr/local/lib/feeder /usr/local/lib/feeder  
  
COPY bin/feeder /usr/local/bin/feeder  
COPY bin/startup /usr/local/bin/startup  
  
WORKDIR /appdata  
RUN mkdir -p config/feeder config/pt logs  
  
RUN \  
addgroup --gid 1000 feeder && \  
adduser --disabled-password --gecos "" \--shell /bin/sh --gid 1000 --uid 1000
ptfuser  
#RUN \  
# addgroup -g 1000 pt && \  
# adduser -D -s /bin/sh -G pt -u 1000 ptuser  
RUN chown -R ptfuser:feeder /usr/local/lib/feeder /appdata  
  
VOLUME /appdata/config/feeder  
VOLUME /appdata/config/pt  
VOLUME /appdata/logs  
  
# not used for now  
#EXPOSE 5001  
USER ptfuser  
WORKDIR /appdata  
  
CMD ["startup"]  

