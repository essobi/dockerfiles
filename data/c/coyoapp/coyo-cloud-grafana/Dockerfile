FROM golang:1.10.1-alpine as builder  
WORKDIR /go/src/bitbucket.com/coyoapp/coyo-cloud-grafana-docker/permission-
provisioner/  
  
COPY permission-provisioner .  
RUN CGO_ENABLED=0 go build -a -ldflags '-s' -installsuffix cgo -o permission-
provisioner .  
  
FROM grafana/grafana:5.0.4  
COPY \--from=builder /go/src/bitbucket.com/coyoapp/coyo-cloud-grafana-
docker/permission-provisioner/permission-provisioner /permission-provisioner  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /permission-provisioner /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
COPY provisioning/ /etc/grafana/provisioning  
COPY dashboards /var/lib/grafana/dashboards  
COPY grafana.ini /etc/grafana/grafana.ini  

