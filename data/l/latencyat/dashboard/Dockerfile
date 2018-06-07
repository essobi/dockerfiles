FROM debian  
  
ENV GOPATH /go  
ENV PATH $PATH:/usr/local/go/bin:/go/bin  
ENV GO_VERSION 1.8.3  
ENV GO_DL_URL https://storage.googleapis.com/golang/go${GO_VERSION}.linux-
amd64.tar.gz  
  
RUN apt-get update -qy && \  
apt-get install -qy curl runit git jq && \  
curl -sL $GO_DL_URL | \  
tar -C /usr/local -xzvf -  
  
## Grafana  
ENV GRAFANA_VERSION 4.4.1  
ENV GRAFANA_DL_URL https://s3-us-west-2.amazonaws.com/grafana-
releases/release/grafana-$GRAFANA_VERSION.linux-x64.tar.gz  
RUN mkdir -p /opt/grafana && \  
curl -Lsf $GRAFANA_DL_URL | \  
tar --strip-components 1 -C /opt/grafana -xzvf -  
  
## Prometheus  
ENV PROMETHEUS_VERSION 2.0.0-beta.2  
ENV PROMETHEUS_DL_URL
https://github.com/prometheus/prometheus/releases/download/v${PROMETHEUS_VERSION}/prometheus-${PROMETHEUS_VERSION}.linux-
amd64.tar.gz  
RUN mkdir /opt/prometheus && \  
curl -Lsf $PROMETHEUS_DL_URL | \  
tar --strip-components 1 -C /opt/prometheus -xzvf -  
  
ENV GF_SECURITY_ADMIN_USER admin  
ENV GF_SECURITY_ADMIN_PASSWORD admin  
  
COPY files/ /etc/  
VOLUME [ "/data" ]  
ENTRYPOINT [ "/etc/entrypoint" ]  
EXPOSE 3000 9090  

