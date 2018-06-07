FROM debian  
  
ENV FTP_USER dev  
ENV FTP_PASSWORD dev  
ENV FTP_UID 1000  
ENV FTP_GID 1000  
ENV FTP_PATH /data/ftp/  
  
RUN export DEBIAN_FRONTEND='noninteractive' && \  
apt-get update -qq && \  
apt-get install -qqy --no-install-recommends vsftpd openssl ssl-cert && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/*  
  
COPY vsftpd.conf /etc/vsftpd.conf  
COPY start.sh /  
  
RUN chmod +x /start.sh  
  
RUN echo "alias l='ls -la'" >> ~/.bashrc  
  
EXPOSE 20 21  
EXPOSE 12020 12021  
#EXPOSE 990  
ENTRYPOINT ["/start.sh"]  

