FROM alpine:3.7  
  
ENV UNISON_VERSION=2.48.4 \  
CHE_HOST= \  
CHE_USER= \  
CHE_PASS= \  
CHE_TOTP= \  
CHE_NAMESPACE= \  
CHE_WORKSPACE= \  
CHE_PROJECT= \  
FORWARD_PORT=9000 \  
SSH_USER=user \  
UNISON=/mount/.unison \  
UNISON_NAME=che-local \  
UNISON_PROFILE= \  
UNISON_REPEAT=watch  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
RUN apk add \--no-cache bash coreutils curl iputils jq ncurses openssh
unison=~${UNISON_VERSION} && \  
addgroup -g 1000 -S user && \  
adduser -u 1000 -DS -h /home/user -s /sbin/nologin -g user -G user user && \  
mkdir /mount /home/user/.ssh && chown user:user /mount /home/user/.ssh  
  
WORKDIR /home/user  
  
USER user  
  
COPY entrypoint.sh /  

