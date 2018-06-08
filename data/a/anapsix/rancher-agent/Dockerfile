# Dockerfile  
FROM alpine:latest  
RUN apk upgrade --update && apk add bash jq tar gzip util-linux procps python
py-pip python-dev libaio bridge-utils curl docker g++ gcc libffi-dev openssl-
dev conntrack-tools && \  
pip install eventlet cattle docker-py && \  
pip install --upgrade requests[security]==2.7.0 && \  
apk del --purge libffi-dev openssl-dev gcc g++ python-dev && \  
echo "The following is required to make nsenter work" >&2 && \  
echo "once Rancher removes nsenter depency, this step can be ommited.." >&2 &&
\  
curl -Ls https://circle-artifacts.com/gh/andyshinn/alpine-pkg-
glibc/6/artifacts/0/home/ubuntu/alpine-pkg-
glibc/packages/x86_64/glibc-2.21-r2.apk > /tmp/glibc-2.21-r2.apk && \  
apk add --allow-untrusted /tmp/glibc-2.21-r2.apk && \  
rm -v /tmp/glibc-2.21-r2.apk  
  
RUN mkdir -p /var/lib/cattle /var/lib/rancher  
COPY register.py resolve_url.py agent.sh run.sh /  
ENTRYPOINT ["/run.sh"]  
LABEL "io.rancher.container.system"="rancher-agent"  
ENV RANCHER_AGENT_IMAGE rancher/agent:v0.7.11  

