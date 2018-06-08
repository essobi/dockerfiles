FROM alpine:3.6  
ARG HUGO_VERSION="0.26"  
ARG TMP_INSTALL="/tmp/hugo"  
ENV APP_DIR="/usr/src/app"  
RUN set -x \  
&& apk add --update --upgrade --no-cache --virtual .install-packages \  
ca-certificates wget \  
&& mkdir -p ${TMP_INSTALL} ${APP_DIR} /usr/local/bin \  
&& cd ${TMP_INSTALL} \  
&& wget
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
\  
&& tar -xzvf hugo_${HUGO_VERSION}_Linux-64bit.tar.gz \  
&& mv hugo /usr/local/bin/hugo \  
&& cd ${HOME} \  
&& rm -rf ${TMP_INSTALL} \  
&& apk del .install-packages  
  
WORKDIR ${APP_DIR}  
  
CMD ["/usr/local/bin/hugo", "server", "-D", "-w", "-p", "5000", "--bind",
"0.0.0.0"]  
  
EXPOSE 5000  

