FROM alpine:latest  
  
# meta  
LABEL \  
org.label-schema.maintainer="me codar nl" \  
org.label-schema.name="unbound" \  
org.label-schema.description="Docker version of Unbound based on Alpine Linux"
\  
org.label-schema.version="1.0" \  
org.label-schema.vcs-url="https://github.com/githubcdr/docker-unbound" \  
org.label-schema.schema-version="1.0"  
  
RUN apk add --update --no-cache unbound curl ca-certificates s6 \  
&& curl -o /etc/unbound/root.hints https://www.internic.net/domain/named.cache  
  
# add files, this also creates the layout for the filesystem  
COPY files/root/ /  
  
# fixups  
RUN chmod a+x /service/*/run  
  
# ready to run  
EXPOSE 53/udp 53/tcp  
  
# manage with s6  
ENTRYPOINT ["/bin/s6-svscan","/service"]  

