FROM alpine:3.7  
COPY slack_blamer.sh /  
  
ENV PACKAGES "bash curl openssl ca-certificates"  
RUN chmod +x /slack_blamer.sh && apk add --update $PACKAGES && rm -rf
/var/cache/apk/*  
  
ENTRYPOINT ["/slack_blamer.sh"]  
  
CMD ["bash"]  

