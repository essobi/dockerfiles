FROM ubuntu:16.04  
ENV DOCKER_PORT 2375  
RUN apt-get update && apt-get install -y socat  
  
EXPOSE ${DOCKER_PORT}/tcp  
  
CMD echo "Starting socat portforward on port ${DOCKER_PORT}" && \  
socat -v TCP-LISTEN:${DOCKER_PORT},reuseaddr,fork UNIX-
CLIENT:/var/run/docker.sock

