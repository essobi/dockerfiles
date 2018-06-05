FROM alpine:latest  
MAINTAINER 2infinite <2infinite@users.noreply.github.com>  
RUN apk --no-cache add transmission-daemon su-exec  
ENTRYPOINT ["nice", "ionice", "-c3", "su-exec", "transmission", "transmission-
daemon", "-f", "--log-error", "--encryption-required" ]  

