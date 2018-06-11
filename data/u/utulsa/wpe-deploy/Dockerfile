FROM alpine:3.5  
RUN apk add --no-cache bash git openssh  
  
## Prevents ssh from asking to verify the host identity  
## http://stackoverflow.com/a/18138352  
RUN echo " IdentityFile ~/.ssh/id_rsa" >> /etc/ssh/ssh_config &&\  
echo " StrictHostKeyChecking no" >> /etc/ssh/ssh_config  
  
COPY bin/* /usr/local/bin/  
  
RUN chmod 111 /usr/local/bin/run-deploy &&\  
chmod 111 /usr/local/bin/setup-ssh  
  
## No entrypoint since we may want to run a script to set up SSH  

