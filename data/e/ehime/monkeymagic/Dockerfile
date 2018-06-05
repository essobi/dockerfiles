FROM java:8  
MAINTAINER ehime <dodomeki@gmail.com>  
  
## Installs insfosec updates  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /simianarmy  
  
## Build the Army  
ENV SIMIANARMY_VERSION v2.5.3  
RUN git clone git://github.com/Netflix/SimianArmy.git . \  
&& git checkout -qf $SIMIANARMY_VERSION \  
&& ./gradlew build  
  
# Set up confd (latest)  
ENV CONFD_VERSION 0.15.0  
RUN curl -fsSL
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 \  
-o /usr/local/bin/confd \  
&& chmod +x /usr/local/bin/confd  
  
COPY confd/ /etc/confd  
  
## Configure and start Simian Army  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
EXPOSE 8080  

