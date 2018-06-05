FROM alpine:3.7  
RUN apk add --update bash curl && rm -rf /var/cache/apk/*  
  
ENV POST_EVERY_MINUTE missing  
  
COPY configure-and-run.sh .  
  
CMD ["/bin/bash", "configure-and-run.sh"]

