FROM frolvlad/alpine-glibc  
# the borg-linux64 executable is hardlinked to glibc default alpine does not
provide it  
ARG BORG_VERSION=1.1.3  
RUN apk update \  
&& apk add --virtual .deps \  
ca-certificates \  
curl \  
&& apk add \  
openssh \  
# && curl -Lo /usr/local/bin/borg \  
# https://github.com/borgbackup/borg/releases/download/${BORG_VERSION}/borg-
linux64 \  
&& curl -Lo /bin/borg \  
https://github.com/borgbackup/borg/releases/download/${BORG_VERSION}/borg-
linux64 \  
&& chmod +x /bin/borg \  
&& cp -r /etc/ssh /etc/ssh.sav \  
&& apk del .deps \  
&& rm -rf \  
/etc/motd \  
/var/cache/apk/*  
  
ADD docker.sh /srv/docker-entry  
  
EXPOSE 22  
ENTRYPOINT ["/srv/docker-entry"]  
CMD ["/usr/sbin/sshd", "-D", "-e"]  

