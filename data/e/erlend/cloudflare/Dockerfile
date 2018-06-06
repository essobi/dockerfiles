FROM alpine:3.5  
ENV CRON_PATTERN="0 * * * *"  
RUN apk add --no-cache curl jq dcron dumb-init && adduser -D cloudflare  
  
COPY update_cf.sh entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  

