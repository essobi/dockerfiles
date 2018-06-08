FROM stakater/base-alpine:3.7  
ARG UID=1000  
ARG GID=1000  
RUN addgroup -g ${GID} kibana-objects && \  
adduser -D -u ${UID} -G kibana-objects kibana-objects  
  
ENV ELASTICSEARCH_URL="http://localhost:9200" \  
RETRY_LIMIT=10  
ADD ./objects /kibana-objects/  
ADD ./scripts /kibana-scripts/  
RUN chmod +x kibana-scripts/*.sh && \  
chown -R kibana-objects:kibana-objects /kibana-objects/ && \  
chown -R kibana-objects:kibana-objects /kibana-scripts/  
  
USER kibana-objects  
  
# Override base image's entrypoint and cmd  
# As the container is supposed to run once and terminate  
CMD [ "/bin/bash", "-c" ]  
ENTRYPOINT [ "/kibana-scripts/put-objects.sh" ]

