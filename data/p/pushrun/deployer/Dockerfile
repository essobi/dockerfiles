# The bare minimum needed for CI deployment scripts. Small to be fast.  
FROM alpine:latest  
RUN apk add --no-cache bash git curl openssh-client sshpass rsync; mkdir -p
~/.ssh; echo 'StrictHostKeyChecking no' >> ~/.ssh/config  

