FROM rubinius/docker:latest  
  
ADD http://curl.haxx.se/ca/cacert.pem /tmp  
  
ENV SSL_CERT_FILE=/tmp/cacert.pem  
  
RUN rbx -S gem install fresh-mc --no-rdoc --no-ri -V  
  
CMD rbx -r fresh-mc  
  

