FROM alpine:3.7  
MAINTAINER Manala <contact@manala.io>  
  
USER root  
  
# Packages  
RUN apk add --no-cache \  
# Entrypoint  
su-exec \  
# Command  
bash \  
# Tools  
curl make git dumb-init  
  
# Goss  
ENV GOSS_VERSION="0.3.5"  
RUN curl -fsSL https://goss.rocks/install | GOSS_VER=v${GOSS_VERSION} sh  
  
# Entrypoint  
COPY entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["entrypoint.sh"]  
  
# Default command  
CMD ["/bin/bash"]  
  
# Working directory  
WORKDIR /srv  
  
########  
# User #  
########  
ARG USER_ID  
ARG GROUP_ID  
  
ENV USER_DEFAULT="deploy" \  
USER_ID="${USER_ID:-1000}" \  
GROUP_DEFAULT="deploy" \  
GROUP_ID="${GROUP_ID:-1000}"  
RUN addgroup -g ${GROUP_ID} ${GROUP_DEFAULT} && \  
adduser -D -s /bin/bash -g ${USER_DEFAULT} -u ${USER_ID} -G ${GROUP_DEFAULT}
${USER_DEFAULT}  
  
##########  
# Custom #  
##########  
# Packages  
RUN apk add --no-cache rsync openssh-client && \  
echo -e "\n\  
Host *\n\  
StrictHostKeyChecking no\n\  
ForwardAgent yes\n\  
UserKnownHostsFile /dev/null\n\  
LogLevel ERROR\n" >> /etc/ssh/ssh_config  

