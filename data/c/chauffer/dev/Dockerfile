FROM alpine  
  
RUN apk add --no-cache \  
git tmux curl tree htop unzip wget bash \  
openssh rsync vim python3 python \  
weechat weechat-perl weechat-python  
  
# wemux  
RUN wget https://raw.githubusercontent.com/zolrath/wemux/master/wemux -O
/usr/local/bin/wemux \  
&& chmod +x /usr/local/bin/wemux  
  
# ssh  
RUN mkdir /root/.ssh \  
&& wget -O /root/.ssh/authorized_keys https://github.com/chauffer.keys \  
&& chown -R root:root /root/.ssh \  
&& chmod -R 0700 /root/.ssh \  
&& mkdir -p ~root/.ssh && chmod 700 ~root/.ssh/ \  
&& echo -e "Port 22\n" >> /etc/ssh/sshd_config \  
&& cp -a /etc/ssh /etc/ssh.cache \  
&& mkdir /rootsshcache \  
&& cp -a /root/.ssh/* /rootsshcache/  
  
COPY entry.sh /entry.sh  
  
VOLUME ["/root", "/home"]  
ENTRYPOINT ["/entry.sh"]  
CMD ["/usr/sbin/sshd", "-D", "-f", "/etc/ssh/sshd_config"]  
  

