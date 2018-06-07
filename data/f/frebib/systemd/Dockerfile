FROM debian:stretch  
  
ENV container=docker  
  
ARG DEBIAN_FRONTEND=noninteractive  
RUN apt-get update -y && \  
apt-get upgrade -y &&\  
apt-get install -y systemd && \  
apt-get clean  
  
# Don't start any optional services except for the few we need.  
# Source: https://github.com/solita/docker-
systemd/blob/a87ced841eeb831a0d0ee5d03d03681f04dcf231/Dockerfile  
RUN find /etc/systemd/system \  
/lib/systemd/system \  
-path '*.wants/*' \  
-not -name '*journald*' \  
-not -name '*systemd-tmpfiles*' \  
-not -name '*systemd-user-sessions*' \  
-exec rm \\{} \;  
  
RUN sed -i 's/#\\(ForwardToConsole=\\).*$/\1yes/' /etc/systemd/journald.conf
&& \  
systemctl set-default multi-user.target  
  
# systemd signal spec:
https://github.com/systemd/systemd/blob/master/src/core/manager.c#L445  
STOPSIGNAL "RTMIN+3"  
ENTRYPOINT ["bash", "-c", "exec /lib/systemd/systemd --log-target=journal
3>&1"]  

