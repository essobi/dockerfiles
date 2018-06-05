FROM alpine  
LABEL maintainer="hackaday <hackaday@coz.moe>"  
  
ENV LANG C.UTF-8  
# Add s6-overlay  
ENV S6_OVERLAY_VERSION=v1.18.1.5  
RUN set -ex \  
&& apk add --no-cache --virtual .fetch-deps \  
curl \  
&& curl -sSL https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz \  
| tar xfz - -C / \  
&& rm -f s6-overlay-amd64.tar.gz \  
&& apk del .fetch-deps  
  
RUN apk add --update --no-cache transmission-daemon openssh nginx  
  
COPY src/ .  
  
RUN set -ex \  
&& mkdir -p /transmission/downloads \  
&& mkdir -p /transmission/incomplete \  
&& mkdir -p /etc/transmission-daemon \  
&& mkdir -p /var/log/nginx \  
&& ln -s /transmission/downloads /opt/web_root/down  
  
RUN set -ex \  
&& ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa \  
&& ssh-keygen -f /etc/ssh/ssh_host_dsa_key -N '' -t dsa \  
&& mkdir -p /var/run/sshd  
  
RUN echo 'root:root' | chpasswd  
  
RUN set -ex \  
&& sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
EXPOSE 22 80 443 9091 51413/tcp 51413/udp  
  
ENV USERNAME admin  
ENV PASSWORD password  
  
WORKDIR /  
  
ENTRYPOINT ["/init"]  
  
CMD []

