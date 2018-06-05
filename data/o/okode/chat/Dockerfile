# Monkeybot  
FROM ubuntu:latest  
  
MAINTAINER Okode <support@okode.com>  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV TERM linux  
  
RUN apt-get -yq update  
  
RUN apt-get install -yq software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get -yq update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-get -yq install oracle-java8-installer && \  
apt-get -yq install unzip  
  
RUN rm -rf /var/lib/apt/lists/*  
  
COPY monkeybot /monkeybot/  
RUN cd monkeybot && ./gradlew build  
  
EXPOSE 8080  
CMD /monkeybot/build/libs/monkeybot-0.1.jar  

