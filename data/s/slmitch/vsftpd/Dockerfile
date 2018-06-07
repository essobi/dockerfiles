FROM alpine:3.7  
LABEL Michel Desconnets "michel.desconnets@gmail.com"  
  
ENV ANONYMOUS_ENABLE=YES \  
ANON_MKDIR_WRITE_ENABLE=NO \  
ANON_UPLOAD_ENABLE=NO \  
FTPUSER_PASSWORD=ftppassword \  
FTPUSER_NAME=ftpuser \  
FTPUSER_UID=1001 \  
LOCAL_UMASK=022 \  
LOG_FTP_PROTOCOL=NO \  
PASV_ADDRESS= \  
PASV_MAX_PORT=30100 \  
PASV_MIN_PORT=30091 \  
TZ=Europe/Paris \  
USE_LOCALTIME=YES \  
VSFTPD_LOG_FILE=/dev/stdout \  
WRITE_ENABLE=YES  
RUN apk add \--update --no-cache tzdata vsftpd && \  
passwd -l root  
  
EXPOSE 21 $PASV_MIN_PORT-$PASV_MAX_PORT  
  
COPY entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

