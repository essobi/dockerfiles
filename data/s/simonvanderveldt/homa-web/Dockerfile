FROM simonvanderveldt/darkhttpd  
ADD https://github.com/bagder/ca-bundle/raw/master/ca-bundle.crt
/etc/ssl/certs/ca-certificates.crt  
ADD https://github.com/simonvanderveldt/getext/releases/download/v0.1.0/getext
/usr/bin/  
RUN ["chmod", "+x", "/usr/bin/getext"]  
RUN ["getext", "https://github.com/binarybucks/homA/archive/master.tar.gz"]  
ENTRYPOINT ["darkhttpd", "/homA-master/interfaces/webinterface"]  

