FROM kalledk/itifn:base  
  
MAINTAINER Kalle R. Møller <docker@k-moeller.dk>  
  
RUN apk add --no-cache \  
dhclient \  
python3 \  
perl  
  
COPY entrypoint.sh /bin/entrypoint.sh  
  
RUN chmod +x /bin/entrypoint.sh  

