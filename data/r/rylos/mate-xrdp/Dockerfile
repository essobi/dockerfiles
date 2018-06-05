FROM debian:buster  
MAINTAINER rylos78@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null  
  
RUN apt-get update && apt-get install -y apt-utils sudo  
RUN apt-get install -y xrdp mate-desktop-environment-core lightdm supervisor
nano dbus-x11 && apt-get clean  
  
COPY supervisord.conf /etc/supervisor/conf.d/xrdp.conf  
COPY Xwrapper.config /etc/X11/Xwrapper.config  
RUN dpkg-reconfigure xserver-xorg-legacy  
# DBus  
RUN mkdir -p /var/run/dbus  
RUN chown messagebus:messagebus /var/run/dbus  
RUN dbus-uuidgen --ensure  
  
RUN useradd -mp sUhVzYQh7odx6 -s /bin/bash -G sudo,xrdp admin  
RUN xrdp-keygen xrdp auto  
  
#RUN echo 'pgrep -U $(id -u) lxsession | grep -v ^$_LXSESSION_PID | xargs
--no-run-if-empty kill' > /bin/lxcleanup.sh  
#RUN chmod +x /bin/lxcleanup.sh  
#RUN echo '@lxcleanup.sh' >> /etc/xdg/lxsession/LXDE/autostart  
CMD ["supervisord", "-n"]  
  
EXPOSE 3389

