FROM alpine:latest  
RUN mkdir -m755 -p /var/www  
ADD https://2ton.com.au/standalone_binaries/rwasa /rwasa  
RUN chmod +x /rwasa  
EXPOSE 80  
ENTRYPOINT ["/rwasa"]  
CMD ["-bind", "80", "-sandbox", "/var/www", "-foreground"]  
  

