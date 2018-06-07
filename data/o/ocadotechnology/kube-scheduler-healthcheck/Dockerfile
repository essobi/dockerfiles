FROM gcr.io/google-containers/exechealthz-amd64:v1.2.0  
USER root:root  
  
RUN apk add --no-cache curl bash jq && \  
curl -L https://storage.googleapis.com/kubernetes-
release/release/v1.9.0/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl && \  
chmod +x /usr/local/bin/kubectl && kubectl version --client && \  
curl -L https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-
init_1.2.1_amd64 -o /usr/local/bin/dumb-init && \  
chmod +x /usr/local/bin/dumb-init  
COPY kube-scheduler-healthcheck /usr/local/bin/  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--", "/exechealthz"]  
CMD ["-port=8090", "-period=60s", "-latency=120s", "-cmd=/usr/local/bin/kube-
scheduler-healthcheck" ]  

