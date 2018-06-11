FROM debian:stable-slim  
  
ARG FUNC_NAME=docker-image-version  
ARG FUNC_PACKAGE=jq  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install curl ${FUNC_PACKAGE} \  
&& echo "Pulling watchdog binary from Github." \  
&& curl -sSL
https://github.com/openfaas/faas/releases/download/0.7.6/fwatchdog >
/usr/bin/fwatchdog \  
&& chmod +x /usr/bin/fwatchdog \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
##CUSTOM  
##CUSTOM  
COPY func.sh /usr/bin/${FUNC_NAME}  
ENV fprocess="/usr/bin/${FUNC_NAME}"  
ENV write_debug="true"  
HEALTHCHECK \--interval=5s CMD [ -e /tmp/.lock ] || exit 1  
CMD [ "fwatchdog" ]  

