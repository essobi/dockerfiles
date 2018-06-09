FROM jbonachera/arch  
RUN useradd --system --uid 797 -M --shell /usr/sbin/nologin transmission  
RUN pacman -S --noconfirm transmission-cli  
RUN mkdir /volumes  
ADD entrypoint.sh /sbin/entrypoint.sh  
VOLUME /var/lib/transmission/Downloads/  
RUN mkdir /etc/transmission-daemon/; chown transmission: /etc/transmission-
daemon/  
RUN mkdir -p /srv/transmission/config; chown transmission:
/srv/transmission/config  
VOLUME /srv/transmission/config  
ADD settings.json /etc/transmission-daemon/settings.json  
USER transmission  
EXPOSE 9091  
CMD /sbin/entrypoint.sh  
  

