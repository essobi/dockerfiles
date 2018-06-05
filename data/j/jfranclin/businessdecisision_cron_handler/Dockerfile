FROM gliderlabs/alpine:3.3  
LABEL maintainer "Joseph FRANCLIN <joseph.franclin@businessdecision.com>"  
  
# Install docker  
RUN apk update && apk add docker jq  
COPY ./run.sh /bin/run.sh  
RUN chmod +x /bin/run.sh  
# Run the first cron 2 minutes after up to update other crons  
RUN echo '*/2 * * * * /bin/run.sh' > /var/spool/cron/crontabs/root  
  
CMD crond -l 2 -f

