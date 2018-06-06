FROM openjdk:8-jdk  
  
MAINTAINER Michael Hahn  
  
ENV TRADE_HOME /opt/trade  
ENV TRADE_VERSION 1.0-SNAPSHOT  
  
ENV PATH ${PATH}:${TRADE_HOME}/bin:${JAVA_HOME}/bin  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update  
RUN apt-get clean  
  
# Copy the sources and build the TraDE source to create required binaries  
COPY . /src  
WORKDIR /src  
RUN ./gradlew build  
  
# Unzip TraDE archive file from /build into ${TRADE_HOME}  
RUN tar -xf /src/build/distributions/traDE-all-${TRADE_VERSION}.tar -C /opt  
RUN ln -s /opt/traDE-all-${TRADE_VERSION} ${TRADE_HOME}  
RUN chmod -R a+x ${TRADE_HOME}/bin/*  
  
# Change the default (Windows-based) persistence directory path to a Linux
path in the config.properties file  
RUN sed -i
's/data.persistence.file.directory=D:\\\\\\\tradeDATA/data.persistence.file.directory=\/tradeData/'
${TRADE_HOME}/config/config.properties  
  
# Change all log levels from DEBUG to INFO in the logback.xml configuration
file  
RUN sed -i 's/DEBUG/INFO/' ${TRADE_HOME}/config/logback.xml  
  
# Clean-up source code & gradle cache  
RUN rm -r /src  
RUN rm -r ~/.gradle  
  
WORKDIR ${TRADE_HOME}  
  
EXPOSE 8081  
ENTRYPOINT [ "traDE" ]  
  
#  
# Build and run:  
#  
# docker build -t trade4chor/trade-core .  
#  
# docker run --name trade-core -p 8081:8081 -d trade4chor/trade-core  
#  
# The container is running in the background and remains active until it is
explicitly stopped by running:  
#  
# docker stop trade-core  
#  
# The middleware is by default configured to run with the local file system as
persistence layer.  
# Nevertheless, the complete middleware can be configured according to users'
requirements and run time context  
# through corresponding files located under 'config/'.  
# To mount customized configuration files located on your host into a
container, start a container with corresponding  
# data volumes (one for the emitted logs and one for the customized
configuration files) through the following command:  
#  
# docker run --name trade-core -p 8081:8081 -d -v
/abs_path_to_persistent_dir/logs:/opt/trade/logs -v
/abs_path_to_persistent_dir/config:/opt/trade/config trade4chor/trade-core  
#  
# As an concrete example on a Windows host:  
# docker run --name trade-core -p 8081:8081 -d -v c:/trade-
data/logs:/opt/trade/logs -v c:/trade-data/config:/opt/trade/config
trade4chor/trade-core  
# ... and on a Linux host:  
# docker run --name trade-core -p 8081:8081 -d -v /trade-
data/logs:/opt/trade/logs -v /trade-data/config:/opt/trade/config
trade4chor/trade-core  
#  
# Templates for all required configuration files can be downloaded from
GitHub: https://github.com/traDE4chor/trade-core/tree/master/config.  
# Please provide all files through the shared host directory in order to run
the middleware correctly.  
# Further details about mounting host directories as data volumes are provided
here: https://docs.docker.com/engine/tutorials/dockervolumes/#mount-a-host-
directory-as-a-data-volume  
# Don't forget to restart/recreate the trade-core container after changing the
configuration so that the changes are applied.  
#  
# As an alternative option, a customized image can be build as provided by
Dockerfile-db which uses MongoDB as  
# persistence layer. To run both services, TraDE and MongoDB, a corresponding
docker-compose.yml is provided as an example.  
#  
#  
# Interactive access for debugging:  
#  
# docker run --rm --name trade-core -p 8081:8081 -ti --entrypoint "/bin/bash"
trade4chor/trade-core  
#  
# Inside the container, the TraDE middleware has to be started manually
through "traDE". In order to be able to use  
# the shell after the middleware is started, the following command allows
running the middleware in the background:  
#  
# nohup traDE &  
#

