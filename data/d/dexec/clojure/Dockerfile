FROM debian:8.0  
MAINTAINER andystanton  
ENV LEIN_EXEC_VERSION 0.3.4  
ENV LEIN_ROOT 1  
RUN apt-get update -qq -y && \  
apt-get install -y patch wget ca-certificates openjdk-7-jre-headless && \  
wget https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
-P /usr/bin && \  
chmod +x /usr/bin/lein && \  
mkdir -p ${HOME}/.lein && echo "{:user {:plugins [[lein-exec
\"${LEIN_EXEC_VERSION}\"]]}}" > ${HOME}/.lein/profiles.clj && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN lein -v  
ADD image-common /tmp/dexec/image-common  
VOLUME /tmp/dexec/build  
ENTRYPOINT ["/tmp/dexec/image-common/dexec-script.sh", "lein exec"]  

