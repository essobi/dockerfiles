FROM stakater/base-alpine:3.7  
ARG UID=1000  
ARG GID=1000  
RUN addgroup -g ${GID} es-template && \  
adduser -D -u ${UID} -G es-template es-template  
  
ENV ELASTICSEARCH_URL="http://localhost:9200" \  
RETRY_LIMIT=10 \  
TEMPLATE_FILE_NAME=logs-template.json \  
TEMPLATE_NAME=logs  
  
ADD ./config /es-template/config  
ADD ./scripts /es-template/scripts  
RUN chmod +x /es-template/scripts/*.sh && \  
chown -R es-template:es-template /es-template/  
  
USER es-template  
  
# Override base image's entrypoint and cmd  
# As the container is supposed to run once and terminate  
CMD [ "/bin/bash", "-c" ]  
ENTRYPOINT [ "/es-template/scripts/put-template.sh" ]

