FROM alpine:edge  
  
ARG NODE_ENV=production  
ARG NODE_HOME=/app  
ARG NODE_USER=nobody  
ARG NPM_LOGLEVEL=warn  
  
RUN apk -U --no-cache upgrade \  
&& apk --no-cache add nodejs ca-certificates \  
&& rm -rf /tmp/* /var/cache/apk/* \  
&& mkdir -p ${NODE_HOME} \  
&& chown -R ${NODE_USER} ${NODE_HOME}  
  
ENV NPM_CONFIG_LOGLEVEL ${NPM_LOGLEVEL}  
ENV NODE_ENV ${NODE_ENV}  
ENV HOME ${NODE_HOME}  
  
WORKDIR ${NODE_HOME}  
  
VOLUME [ "${NODE_HOME}" ]  
  
USER ${NODE_USER}  
  
CMD [ "node" ]  

