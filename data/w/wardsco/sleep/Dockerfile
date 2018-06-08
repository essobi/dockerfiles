FROM alpine  
  
RUN apk add --no-cache coreutils  
ENTRYPOINT ["sh", "-c"]  
CMD ["trap : TERM INT; sleep infinity & wait"]  

