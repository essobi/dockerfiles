FROM debian:jessie  
MAINTAINER "Tristan Seligmann <mithrandi@mithrandi.net>"  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -qy
openjdk-7-jre-headless curl  
ENV LEIN_ROOT 1  
RUN curl -L -s
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein > \  
/usr/local/bin/lein \  
&& chmod 0755 /usr/local/bin/lein \  
&& lein upgrade  
WORKDIR /lein  
ENTRYPOINT ["/usr/local/bin/lein"]  

