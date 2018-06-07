FROM alpine:3.3  
  
RUN apk --update add git \  
perl \  
openssh && \  
mkdir -p /root/.ssh && \  
chmod 700 /root/.ssh && \  
ssh-keyscan github.com bitbucket.org gitlab.com >> /root/.ssh/known_hosts && \  
echo "Host github.com \  
VerifyHostKeyDNS=yes" > /root/.ssh/config && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["git"]  

