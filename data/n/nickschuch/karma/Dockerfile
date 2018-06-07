FROM scratch  
  
ADD karma-0.0.3 /karma  
  
COPY ./certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt  
  
EXPOSE 80  
CMD ["/karma"]  

