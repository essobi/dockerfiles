FROM alpine  
  
MAINTAINER Andrei Miulescu <lusu777@gmail.com>  
  
RUN apk --no-cache add git curl ca-certificates bash openssh-client  
# Security fix for CVE-2016-0777 and CVE-2016-0778  
RUN echo -e 'Host *\nUseRoaming no' >> /etc/ssh/ssh_config  
  
COPY scripts/* /usr/bin/  
  
ENTRYPOINT ["/bin/bash", "-c"]

