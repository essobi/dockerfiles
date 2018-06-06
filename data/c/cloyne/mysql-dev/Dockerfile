FROM tozd/mysql:5.5  
# When running inside boot2docker using VirtualBox Guest Additions, files'
permissions and ownership  
# cannot be really modified, so we make MySQL run as root, which is OK for
development  
RUN sed -i 's/user.*=.*mysql/user = root/' /etc/mysql/my.cnf  
  
COPY ./etc /etc  

