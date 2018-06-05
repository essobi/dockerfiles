FROM debian:jessie-backports  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -t
jessie-backports -qy duplicity python-boto  
COPY ["duplicity-wrapper", "/usr/bin/duplicity-wrapper"]  
ENTRYPOINT ["/usr/bin/duplicity-wrapper"]  

