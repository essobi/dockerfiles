FROM alpine  
  
COPY ./usr-local-bin/ /usr/local/bin/  
  
ENV FTPSYNC_FTP_USER **None**  
ENV FTPSYNC_FTP_USER_FILE **None**  
ENV FTPSYNC_FTP_PASSWORD **None**  
ENV FTPSYNC_FTP_PASSWORD_FILE **None**  
  
ENV FTPSYNC_FTP_HOST **None**  
ENV FTPSYNC_SOURCE_FOLDER **None**  
  
ENV FTPSYNC_MIRROR_OPTIONS --continue --delete --parallel=1 \--loop
--verbose=0  
ENV FTPSYNC_TARGET_FOLDER **None**  
ENV FTPSYNC_CRON_ENTRY **None**  
  
RUN install.sh && \  
rm /usr/local/bin/install.sh  
  
CMD run.sh  

