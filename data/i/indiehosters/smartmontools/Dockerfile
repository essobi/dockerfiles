FROM alpine  
  
RUN apk add --no-cache bash smartmontools  
COPY cron /usr/local/bin/  
COPY smartmon-prom /usr/local/bin/  
COPY short-test /usr/local/bin/  
COPY long-test /usr/local/bin/  

