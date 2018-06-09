# The workspace image is a minimal environment for technical work.  
#  
# TODO(hkjn): Consider adding back emacs + configs, once it's been fixed to
work with musl and Alpine has a package:  
# http://forum.alpinelinux.org/forum/general-discussion/cant-find-emacs-
package  
#  
FROM hkjn/alpine  
  
MAINTAINER Henrik Jonsson <me@hkjn.me>  
  
ENV UNPRIVILEGED_UID=500 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8 \  
LC_ALL=en_US.UTF-8 \  
GOSU_VERSION=1.10 \  
GOSU_KEY=B42F6819007F00F88E364FD4036A9C25BF357DD4  
  
COPY start /usr/local/bin/  
  
RUN apk add --no-cache bash git go python py2-pip openssh sudo tmux vim && \  
adduser -D user -u $UNPRIVILEGED_UID -s /bin/bash && \  
echo "user ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/user_sudo && \  
mkdir /home/user/.ssh && \  
chmod 700 /home/user/.ssh && \  
chown -R user:user /home/user && \  
passwd -u user  
  
RUN echo 'Happy haxxing!' > /etc/motd  
  
WORKDIR /home/user  
  
USER user  
RUN mkdir -p src/hkjn.me && \  
cd src/hkjn.me && \  
git clone https://github.com/hkjn/scripts && \  
git clone https://github.com/hkjn/dotfiles && \  
cd dotfiles && \  
cp .bash* ~/  
  
USER root  
  
ENTRYPOINT ["start"]  

