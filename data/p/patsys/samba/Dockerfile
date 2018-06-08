FROM alpine:latest  
MAINTAINER Patrick Weber <pat.weber91@gmail.com>  
COPY update.sh /etc/  
RUN chmod ugo+x /etc/update.sh  
RUN apk update && apk upgrade && apk add coreutils samba-dc krb5 && rm -rf
/var/cache/apk/*  
RUN ln -sf /var/lib/samba/private/krb5.conf /etc/krb5.conf  
# Add startup scripts  
RUN mkdir -p /etc/my_init.d  
COPY samba_setup.sh /etc/my_init.d/  
RUN chmod ugo+x /etc/my_init.d/samba_setup.sh  
  
# Add services  
RUN mkdir -p /etc/service/samba  
COPY samba_run.sh /etc/service/samba/run  
COPY samba_finish.sh /etc/service/samba/finish  
COPY smb.conf /etc/samba/  
COPY samba /etc/init.d/  
COPY start /etc/  
RUN chmod ugo+x /etc/start  
VOLUME ["/var/lib/samba"]  
EXPOSE 53  
EXPOSE 445  
CMD ["/etc/start"]  

