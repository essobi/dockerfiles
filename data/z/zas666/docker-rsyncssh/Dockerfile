FROM alpine:3.2  
MAINTAINER Laurent Monin <zas+docker@metabrainz.org>  
  
RUN apk --update add \  
bash \  
rsync \  
openssh \  
perl && \  
rm -rf /var/cache/apk/* \  
&& ln -sf /usr/share/zoneinfo/UTC /etc/localtime \  
&& rc-update add rsyncd boot  
  
COPY sshd_config /etc/ssh/sshd_config  
  
COPY rrsync /usr/local/bin/  
COPY addkeys.sh /usr/local/bin/  
COPY run.sh /  
  
RUN /usr/bin/ssh-keygen -A  
  
WORKDIR /root  
RUN mkdir .ssh && chmod 750 .ssh  
  
# root account has to be unlocked, even though we never use root password  
# sshd is set to UsePAM no (or isnt even compiled with PAM support)  
RUN echo "root:$(dd if=/dev/urandom bs=1 count=4096 2>/dev/null|sha256sum|cut
-d ' ' -f1)" | chpasswd  
  
CMD ["/run.sh"]  
  
VOLUME /data  
EXPOSE 22  

