FROM gyroplast/archbase64:latest  
MAINTAINER Dennis Herbrich <herbrich@veloxis.de>  
  
RUN pacman -Syu privoxy --noconfirm  
COPY ["privoxy.config", "/etc/privoxy/config"]  
RUN chown privoxy.privoxy /etc/privoxy/config && chmod 0400
/etc/privoxy/config  
  
EXPOSE 8118  
USER privoxy  
  
ENTRYPOINT ["/usr/sbin/privoxy", "--no-daemon", "/etc/privoxy/config"]  

