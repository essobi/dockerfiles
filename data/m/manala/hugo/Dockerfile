FROM alpine:3.7  
MAINTAINER Manala <contact@manala.io>  
  
USER root  
  
# Packages  
RUN apk add --no-cache \  
# System  
sudo su-exec \  
# Command  
bash bash-completion \  
# Tools  
curl make git dumb-init  
  
# Goss  
ENV GOSS_VERSION="0.3.5"  
RUN curl -fsSL https://goss.rocks/install | GOSS_VER=v${GOSS_VERSION} sh  
  
# Entrypoint  
COPY entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["entrypoint.sh"]  
  
# Shell  
CMD ["/bin/bash"]  
  
# Working directory  
WORKDIR /srv  
  
########  
# User #  
########  
ARG USER_ID  
ARG GROUP_ID  
  
ENV USER_DEFAULT="manala" \  
USER_ID="${USER_ID:-1000}" \  
USER_SUDO="1" \  
GROUP_DEFAULT="manala" \  
GROUP_ID="${GROUP_ID:-1000}"  
RUN addgroup -g ${GROUP_ID} ${GROUP_DEFAULT} && \  
adduser -D -s /bin/bash -g ${USER_DEFAULT} -u ${USER_ID} -G ${GROUP_DEFAULT}
${USER_DEFAULT}  
  
##########  
# Custom #  
##########  
# Packages  
RUN apk add --no-cache nodejs nodejs-npm yarn \  
# Tools  
outils-md5 \  
# Image tools  
optipng libjpeg-turbo-utils imagemagick gifsicle pngquant \  
# Compilation (optipng,gifsicle,pngquant,mozjpeg,...)  
gcc autoconf automake libtool nasm musl-dev zlib-dev libpng-dev \  
# Deploy  
rsync openssh-client && \  
echo -e "\n\  
Host *\n\  
StrictHostKeyChecking no\n\  
ForwardAgent yes\n\  
UserKnownHostsFile /dev/null\n\  
LogLevel ERROR\n" >> /etc/ssh/ssh_config  
  
# Npm packages  
ENV SVGO_VERSION="1.0.5"  
RUN npm --global install \  
svgo@${SVGO_VERSION} \  
&& rm -rf /root/.npm  
  
# Hugo  
ENV HUGO_VERSION="0.40.3"  
RUN curl -L
https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
\  
| tar -zxvf - -C /tmp && \  
mv /tmp/hugo /usr/local/bin/hugo && \  
rm -Rf /tmp/hugo_${HUGO_VERSION}_linux_amd64  
  
# Expose default hugo port  
EXPOSE 1313  

