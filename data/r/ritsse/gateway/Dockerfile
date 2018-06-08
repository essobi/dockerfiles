FROM abiosoft/caddy  
  
COPY /Caddyfile /etc/Caddyfile  
  
RUN mkdir -p /root/certs  
  
WORKDIR /root  
ENTRYPOINT ["/usr/bin/caddy"]  
CMD ["--conf", "/etc/Caddyfile", "--email", "tech@sse.rit.edu"]  

