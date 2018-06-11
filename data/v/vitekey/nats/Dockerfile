FROM nats:latest  
  
LABEL author="Iván Anticona <dev@ryam4u.com>"  
  
LABEL organization="VITEKEY"  
  
COPY gnatsd.conf gnatsd.conf  
  
ENTRYPOINT ["/gnatsd"]  
  
CMD ["-c", "gnatsd.conf"]

