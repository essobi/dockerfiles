FROM webhippie/steamcmd:latest  
MAINTAINER Jimmy Lau <stamp1024@gmail.com>  
  
WORKDIR /dst-server  
ENTRYPOINT ["/usr/bin/entrypoint"]  
CMD ["/bin/s6-svscan", "/etc/s6"]  
  
EXPOSE 10888/udp  
VOLUME ["/dst-server/DoNotStarveTogether"]  
ADD rootfs /  
  
RUN chown -R steam:steam \  
/dst-server  
  
RUN /usr/bin/steamcmd \  
+login anonymous \  
+force_install_dir /dst-server \  
+app_update 343050 validate \  
+quit  
  
RUN apt-get update && \  
apt-get install -y libcurl4-gnutls-dev:i386 && \  
apt-get clean  

