FROM debian:latest  
MAINTAINER Aleksey @soar Smyrnov (//soar.name)  
  
ARG RUNDECK_PACKAGE_NAME=rundeck_2.10.6-1-GA_all.deb  
  
RUN apt-get update \  
&& apt-get install -yq --no-install-recommends --no-install-suggests \  
curl \  
openjdk-8-jdk-headless \  
openjdk-8-jre-headless \  
openssh-client \  
uuid-runtime \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl --silent -LO "http://dl.bintray.com/rundeck/rundeck-
deb/${RUNDECK_PACKAGE_NAME}" \  
&& dpkg -i ${RUNDECK_PACKAGE_NAME} \  
&& rm ${RUNDECK_PACKAGE_NAME}  
  
COPY . .  
  
RUN unipatcher/unipatcher.sh && rm -rf unipatcher  
  
# All volumes are commented out, see:  
# https://github.com/moby/moby/issues/3465  
# https://github.com/moby/moby/pull/8177  
# Base configurations directory  
# VOLUME [ "/etc/rundeck" ]  
# Projects directory  
# VOLUME [ "/var/rundeck" ]  
# Work directory - I think it shouldn't be volume  
# VOLUME [ "/var/lib/rundeck" ]  
CMD [ "./run.sh" ]  

