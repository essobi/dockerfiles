# IMAGE masteryconnect/honeybadger-s3:1.0  
# Start from apline, a minimal docker image  
FROM alpine:3.2  
# Add in SSL certificates for use with https and docker-cron  
RUN \  
apk --update upgrade && \  
apk add --update ca-certificates && \  
update-ca-certificates && \  
wget -O /usr/local/bin/docker-cron https://github.com/MasteryConnect/docker-
cron/releases/download/v1.3/docker-cron && \  
wget -O /usr/local/bin/honeybadger-s3
https://github.com/MasteryConnect/honeybadger-s3/releases/download/v1.0/honeybadger-s3
&& \  
chmod +x /usr/local/bin/docker-cron && \  
chmod +x /usr/local/bin/honeybadger-s3 && \  
rm -rf /var/cache/apk/*  
  
# # Copy the pre-built go executable and the static files  
# ADD ./bin/honeybadger-s3 /usr/local/bin/  
# Run the honeybadger-s3 command by default when the container starts using  
# docker-cron to run it periodically. Use environment variables passed in  
# to configure both docker-cron and honeybadger-s3 processes.  
CMD ["/usr/local/bin/docker-cron", "/usr/local/bin/honeybadger-s3"]  

