FROM alpine:3.2  
RUN apk update && \  
apk add socat && \  
rm -r /var/cache/*  
  
# Not really necessary for our purposes  
EXPOSE 2375  
# -t is needed because of https://github.com/docker/docker/issues/16602  
ENTRYPOINT ["socat", "-t", "100000000", "TCP-LISTEN:2375,reuseaddr,fork",
"UNIX:/docker.sock"]  

