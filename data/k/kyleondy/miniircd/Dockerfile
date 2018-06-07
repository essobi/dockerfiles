FROM gliderlabs/alpine:3.4  
RUN apk add --no-cache python  
  
ADD https://raw.githubusercontent.com/jrosdahl/miniircd/master/miniircd /app/  
ADD motd /app/  
RUN chmod +x /app/miniircd  
  
EXPOSE 6667  
ENTRYPOINT [ "/app/miniircd" ]  
CMD [ "--setuid", "root", "--debug", "--verbose", "--motd", "/app/motd" ]  
  

