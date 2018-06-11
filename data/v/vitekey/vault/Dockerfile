FROM vault:0.10.1  
LABEL author="Iván Anticona <dev@ryam4u.com>"  
  
LABEL organization="VITEKEY"  
  
COPY ./config/* /vault/config/  
  
ENTRYPOINT ["/bin/vault", "server", "-config=/vault/config/server.json"]

