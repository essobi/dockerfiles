FROM scratch  
MAINTAINER Marcel Huber <marcelhuberfoo@gmail.com>  
  
ADD arch-rootfs-20160107-4.3.3-2.tar.xz /  
  
USER root  
  
# allow use of gosu to execute commands as different user  
RUN mkdir -p /usr/local/bin && \  
curl -o /usr/local/bin/gosu -sSL
https://github.com/tianon/gosu/releases/download/1.7/gosu-amd64 && \  
chmod +x /usr/local/bin/gosu  
  
RUN pacman -Syy && \  
printf "\\\ny\\\ny\\\n" | pacman -S sudo vim-minimal && \  
printf "y\\\ny\\\n" | pacman -Scc && rm -f /var/lib/pacman/sync/*.db  
  
ENV EDITOR=vim \  
UNAME=nobody \  
GNAME=nobody \  
LANG=en_US.utf8  
  
# prepare non root user  
RUN mkdir /$UNAME && usermod --home /$UNAME $UNAME  
RUN sed -r -e '/If not.*/ d' -e '/\\*i\\*/ d' /etc/skel/.bashrc
>$UNAME/.bashrc && ln -s -r $UNAME/.bashrc $UNAME/.bash_profile && echo -e
"umask 0002\ncd \$HOME\n" >> $UNAME/.bashrc  
RUN chown -R $UNAME:$GNAME /$UNAME  
ADD sudo_USER /etc/sudoers.d/$UNAME  
RUN sed -i "s|USER|$UNAME|" /etc/sudoers.d/$UNAME && chmod 0440
/etc/sudoers.d/$UNAME  
  
CMD ["/bin/bash"]  
  

