FROM alpine  
RUN apk update  
RUN apk add transmission-daemon gettext  
RUN mkdir -p /var/lib/transmission /etc/transmission  
ENV RPC_PASSWORD nopasswd  
VOLUME /var/lib/transmission  
EXPOSE 80  
EXPOSE 51413  
CMD ["/start.sh"]  
COPY settings.json /etc/transmission/settings.json  
COPY start.sh /  

