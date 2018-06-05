FROM alpine:edge  
MAINTAINER Chaitanya Akkineni  
  
RUN echo '@testing http://nl.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories && \  
apk update && \  
apk add --no-cache bash jq curl bats@testing && \  
rm -rf /var/cache/apk/*  
  
ADD tests /tests  
ADD run.sh /bin  
CMD /bin/run.sh  
ENTRYPOINT ["/bin/run.sh"]

