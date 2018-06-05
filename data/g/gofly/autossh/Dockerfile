FROM alpine:3.5  
RUN apk add --no-cache autossh  
ENV SSH_PORT="22" \  
SSH_USER="root" \  
SSH_ID_RSA="" \  
SSH_HOST="127.0.0.1" \  
SSH_TUNNEL_RULES="" \  
AUTOSSH_PORT="20000"  
COPY docker-entrypoint.sh /  
RUN chmod 755 /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["autossh"]  

