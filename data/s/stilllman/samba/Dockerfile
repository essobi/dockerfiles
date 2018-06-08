# Run with  
# docker run -it -p 137-139:137-139 -p 445:445 -v <data folder>:/data --name
samba stilllman/samba  
# (not sure yet why -it is needed)  
# The only user available is "samba". The default password is "samba", it can
be changed  
# by passing the environment variable SAMBA_PASSWORD when running the
container.  
FROM alpine:3.4  
RUN apk add --no-cache samba samba-common-tools  
RUN adduser -SDH samba samba  
COPY smb.conf /etc/samba/smb.conf  
  
EXPOSE 137 138 139 445  
COPY samba.sh /usr/local/bin/samba.sh  
ENTRYPOINT ["/usr/local/bin/samba.sh"]  
CMD ["-FS"]  

