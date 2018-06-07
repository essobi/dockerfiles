FROM alpine:edge  
MAINTAINER shun  
  
EXPOSE 22  
  
ENV DOCKER_VERSION 17.09.0-ce  
  
RUN apk add --update \  
curl \  
openssh \  
openssh-client \  
git \  
less \  
grep \  
sudo \  
shadow \  
tzdata \  
tmux \  
bash \  
zsh \  
perl \  
neovim \  
the_silver_searcher \  
python3 \  
py3-pip \  
gcc \  
python3-dev \  
musl-dev \  
&& \  
pip3 install neovim && \  
apk del \  
py3-pip \  
gcc \  
python3-dev \  
musl-dev \  
&& \  
addgroup -S sudo && \  
echo '%sudo ALL=(ALL:ALL) NOPASSWD: ALL' >> /etc/sudoers && \  
curl
https://download.docker.com/linux/static/stable/x86_64/docker-$DOCKER_VERSION.tgz
--output /tmp/docker.tgz && \  
tar -xzf /tmp/docker.tgz -C /tmp && \  
mv /tmp/docker/docker /usr/local/bin && \  
rm -rf /tmp/docker* && \  
:  
  
COPY docker-entrypoint.sh labo-setup /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["/usr/sbin/sshd","-D"]  

