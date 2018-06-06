FROM charliev5/alpineedge  
MAINTAINER Charlie Wang <272876047@qq.com>  
  
ADD apk /tmp/apk  
RUN cp /tmp/apk/-57cfc5fa.rsa.pub /etc/apk/keys  
  
# git  
RUN apk --update add git  
  
#python  
RUN apk add python  
  
#repo  
RUN apk add curl && curl https://storage.googleapis.com/git-repo-
downloads/repo > /bin/repo && chmod a+x /bin/repo && apk del curl  
  
# Todo: Switch from string literals to env vars, and in the CMD, quit with
error if the aren't set from the outside  
RUN git config --global color.ui false  
RUN git config --global user.email "test@test.net"  
RUN git config --global user.name "Test McTesterson"  
  
RUN apk --update --no-cache add xrdp xvfb alpine-desktop xfce4 thunar-volman \  
faenza-icon-theme slim xf86-input-synaptics xf86-input-mouse xf86-input-
keyboard \  
setxkbmap sudo util-linux dbus wireshark ttf-freefont xauth supervisor
busybox-suid openssl nano\  
&& apk add /tmp/apk/ossp-uuid-1.6.2-r0.apk \  
&& apk add /tmp/apk/ossp-uuid-dev-1.6.2-r0.apk \  
&& apk add /tmp/apk/x11vnc-0.9.13-r0.apk \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
RUN mkdir ~/shashlik  
ENV platform linux  
RUN cd ~/shashlik && repo init -u https://github.com/shashlik/shashlik-
manifest -p $platform  
CMD cd ~/shashlik && repo sync  
  
ADD etc /etc  
  
RUN xrdp-keygen xrdp auto  
RUN sed -i '/TerminalServerUsers/d' /etc/xrdp/sesman.ini \  
&& sed -i '/TerminalServerAdmins/d' /etc/xrdp/sesman.ini  
  
EXPOSE 3389 22  
#WORKDIR /home/alpine  
#USER alpine xrdp  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["/usr/bin/supervisord","-c","/etc/supervisord.conf"]  

