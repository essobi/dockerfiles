FROM alpine:3.7  
RUN wget https://pkg.cfssl.org/R1.2/cfssl_linux-amd64 -O /usr/local/bin/cfssl
&& chmod +x /usr/local/bin/cfssl && \  
wget https://pkg.cfssl.org/R1.2/cfssljson_linux-amd64 -O
/usr/local/bin/cfssljson && chmod +x /usr/local/bin/cfssljson && \  
mkdir /data  
  
WORKDIR /data  
  
CMD ["cfssl"]  

