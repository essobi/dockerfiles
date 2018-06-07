FROM alpine:3.6  
# Get curl  
RUN apk add --no-cache curl rsync  
  
# Add in any scripts we need  
RUN mkdir -p /srv  
COPY is_factomd_up.sh is_shepard_up.sh is_wallet_up.sh /srv/  
  

