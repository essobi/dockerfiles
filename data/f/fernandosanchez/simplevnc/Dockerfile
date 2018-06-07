FROM boggart/alpine-apk-static-32bit  
  
MAINTAINER Boggart "github.com/Boggart"  
RUN ["/sbin/apk.static", "add", "--update", "alpine-base", "pwgen", "xvfb", \  
"linux-pam", "wget","supervisor","perl", "xfce4"]  
  
RUN wget --no-check-certificate
"https://dl.dropboxusercontent.com/u/83869314/ShareX/2015/05/glibc-2.21-r4.apk"
&& \  
apk.static add --allow-untrusted glibc-2.21-r4.apk && \  
wget --no-check-certificate
"https://dl.dropboxusercontent.com/u/83869314/ShareX/2015/05/glibc-
bin-2.21-r4.apk" && \  
apk.static add --allow-untrusted glibc-bin-2.21-r4.apk && \  
/usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib && \  
rm -rf /var/cache/apk/* && \  
wget --no-check-certificate
https://bintray.com/artifact/download/tigervnc/stable/tigervnc-
Linux-i686-1.4.3.tar.gz && tar zxf tigervnc-Linux-i686-1.4.3.tar.gz ./usr -C /
&& rm tigervnc-Linux-i686-1.4.3.tar.gz && \  
adduser -D -s /bin/bash vncer  
  
ENV HOME /home/vncer  
WORKDIR /home/vncer/  
  
ENV DISPLAY :0  
# Expose the default port  
# FIXME: expose $PORT0 if it exists  
EXPOSE 5900  
COPY ./assets/supervisor/supervisord.conf /etc/supervisord.conf  
RUN su -c "mkdir /etc/supervisord/"  
  
COPY ./assets/supervisor/vncserver.conf /etc/supervisord/  
COPY ./assets/supervisor/xvfb.conf /etc/supervisord/  
COPY ./assets/supervisor/xfce4.conf /etc/supervisord/  
  
RUN su -c "chmod 775 /etc/supervisord/*.*"  
  
COPY ./assets/start.sh /usr/local/bin/  
RUN su -c "chmod +x /usr/local/bin/start.sh"  
  
# Default execute the entrypoint  
CMD ["/usr/local/bin/start.sh"]  

