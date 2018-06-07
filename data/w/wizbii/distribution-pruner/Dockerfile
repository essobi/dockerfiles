FROM golang:latest  
RUN go get -u gitlab.com/gitlab-org/docker-distribution-pruner  
  
FROM alpine:latest  
COPY \--from=0 /go/bin/docker-distribution-pruner .  
CMD ["/lib/ld-musl-x86_64.so.1","./docker-distribution-
pruner","-config","/etc/docker/registry/config.yml", "-ignore-blobs",
"-parallel-blob-walk", "-soft-errors", "-delete", "-soft-delete", "false"]  

