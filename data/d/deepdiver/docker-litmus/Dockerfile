FROM alpine  
  
RUN apk --update add tar curl bash g++ make openssl-dev  
  
# Install Litmus  
ADD http://www.webdav.org/neon/litmus/litmus-0.13.tar.gz
/tmp/litmus/litmus.tar  
  
RUN tar -xvf /tmp/litmus/litmus.tar && \  
rm /tmp/litmus/litmus.tar && \  
mv litmus-0.13 litmus && \  
cd /litmus && \  
./configure --with-ssl && \  
make install  
  
# Test with something like: make URL=http://192.168.64.7/ CREDS="foo bar"
check  

