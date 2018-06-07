# Build Geth in a stock Go builder container  
FROM golang:1.9.2-stretch  
  
RUN apt-get install -y make gcc git  
  
RUN git clone https://github.com/expanse-org/go-expanse.git /go-expanse  
  
WORKDIR /go-expanse  
  
RUN git checkout 'tags/v1.7.2'  
  
RUN make gexp  
  
RUN cp build/bin/gexp /usr/local/bin/  
  
EXPOSE 9656 9656 42786 42786/udp  
  
ADD entrypoint.sh /root/entrypoint.sh  
RUN chmod +x /root/entrypoint.sh  
  
ENTRYPOINT ["/root/entrypoint.sh"]  

