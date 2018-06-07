FROM navyproject/drinking_base  
  
ADD . /var/www  
  
RUN bundle install  
  
ADD navy.crt /usr/local/share/ca-certificates/  
RUN /usr/sbin/update-ca-certificates --fresh  
RUN mkdir -p /etc/pki/tls/certs/  
RUN ln -s /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt  
  
EXPOSE 3000  
CMD rails s  

