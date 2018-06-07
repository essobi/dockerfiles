FROM
alpine:3.7@sha256:8c03bb07a531c53ad7d0f6e7041b64d81f99c6e493cb39abba56d956b40eacbc  
RUN apk --update add \--no-cache openssh-client && \  
addgroup -S sshuser && \  
adduser -S -G sshuser sshuser && \  
mkdir -p /home/sshuser/.ssh && \  
chown sshuser:sshuser /home/sshuser/.ssh && \  
chmod 700 /home/sshuser/.ssh  
USER sshuser  
WORKDIR /home/sshuser  
VOLUME /home/sshuser/.ssh  

