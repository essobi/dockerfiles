FROM ubuntu:trusty  
ENV NO_PROXY .svc.cluster.local,.service.consul  
ARG URL_TO_CURL  
ARG VAULT_SERVER_URL  
RUN apt-get update && apt-get install -y curl jq && apt-get clean && rm -rf
/var/lib/apt/lists  
COPY entrypoint.sh /  
CMD ["/entrypoint.sh"]  

