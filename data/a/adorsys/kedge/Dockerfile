FROM golang  
WORKDIR /  
ADD https://github.com/kedgeproject/kedge/releases/download/v0.4.0/kedge-
linux-amd64.tar.gz /  
RUN tar xvf /kedge-linux-amd64.tar.gz  
RUN chmod +x /kedge-linux-amd64  
RUN chown 0:0 /kedge-linux-amd64  
CMD ["/kedge-linux-amd64"]  

