FROM stilliard/pure-ftpd  
  
ENV PUBLICHOST colorbyamber.com  
  
# Change the user and group of the FTP user to match that of the deploy user
on the server  
RUN usermod -u 1001 ftpuser \  
&& groupmod -g 1001 ftpgroup  
  

