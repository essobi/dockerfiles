FROM alpine:3.6  
RUN mkdir -p /nsq-chunked-mails  
COPY data.tar /nsq-chunked-mails/data.tar  
  
WORKDIR /nsq-chunked-mails  
RUN tar -xf data.tar -C /nsq-chunked-mails && chmod +x /nsq-chunked-
mails/nsq_chunked_mails  
  
CMD ["/nsq-chunked-mails/nsq_chunked_mails"]  

