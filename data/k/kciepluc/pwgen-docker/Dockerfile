FROM alpine:latest  
RUN apk add --no-cache pwgen  
  
# always generate 'secure' passwords  
ENTRYPOINT ["pwgen", "-s"]  
  
# by default, generate 10 different passwords, each one 16-characters long  
CMD ["16", "10"]  

