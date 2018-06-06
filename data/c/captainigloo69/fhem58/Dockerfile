FROM debian:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install packages APT  
RUN apt-get update  
RUN apt-get -y --force-yes install supervisor cron telnet wget curl vim git
nano make gcc g++ apt-transport-https sudo logrotate  
RUN apt-get -y --force-yes install procps uptimed gnupg2 apt-utils net-tools
usbutils  
  
# Install perl packages  
RUN apt-get -y --force-yes install libalgorithm-merge-perl \  
libclass-isa-perl \  
libcommon-sense-perl \  
libdpkg-perl \  
liberror-perl \  
libfile-copy-recursive-perl \  
libfile-fcntllock-perl \  
libio-socket-ip-perl \  
libjson-perl \  
libnet-telnet-perl \  
libjson-xs-perl \  
libmail-sendmail-perl \  
libsocket-perl \  
libswitch-perl \  
libsys-hostname-long-perl \  
libterm-readkey-perl \  
libterm-readline-perl-perl \  
libdevice-serialport-perl \  
libio-socket-ssl-perl \  
libwww-perl \  
libcgi-pm-perl \  
sqlite3 \  
libdbd-sqlite3-perl \  
libtext-diff-perl  
  
# Install DPKG fhem https://debian.fhem.de/fhem.deb  
RUN wget http://fhem.de/fhem-5.8.deb  
RUN dpkg -i fhem-5.8.deb  
RUN apt-get install -f  
  
# Enabled writing mode Fhem web  
RUN echo 'attr WEB editConfig 1' >> /opt/fhem/fhem.cfg  
  
# Create log directory  
RUN mkdir -p /var/log/supervisor  
  
# Setup Logrotate + log  
COPY logrotate.conf /etc/logrotate.conf  
# Create the log file to be able to run tail  
RUN touch /var/log/cron.log  
# Setup cron job  
RUN (crontab -l ; echo "* * */5 * 0 /usr/sbin/logrotate /etc/logrotate.conf >>
/var/log/cron.log") | crontab  
# Run the command on container startup  
CMD cron start  
  
# Setup TZ  
RUN echo Europe/Paris > /etc/timezone dpkg-reconfigure -f noninteractive
tzdata  
  
# Setup sshd on port 2222 and allow root login / password = fhem58  
RUN apt-get -y --force-yes install openssh-server  
RUN echo "root:fhem58" | chpasswd  
RUN /bin/rm /etc/ssh/ssh_host_*  
RUN /bin/rm /etc/ssh/sshd_config  
COPY sshd_config /etc/ssh/sshd_config  
# Execute command in console : dpkg-reconfigure openssh-server  
# Execute command in console : /etc/init.d/ssh start  
# Cleaning APT  
RUN apt-get clean  
  
# supervisord.conf for supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Owner fhem.cfg  
RUN chown fhem /opt/fhem/fhem.cfg  
  
EXPOSE 2222 7072 8083 8084 8085  
CMD ["/usr/bin/supervisord"]  

