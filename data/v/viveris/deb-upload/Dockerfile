FROM valudio/docker-sshpass:alpine  
ADD deb_upload.sh /deb_upload.sh  
RUN chmod +x /deb_upload.sh  
ENTRYPOINT ["/deb_upload.sh"]  

