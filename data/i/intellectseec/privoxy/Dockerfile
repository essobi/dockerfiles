FROM alpine:latest  
  
RUN apk --no-cache add \  
privoxy  
  
EXPOSE 8118  
  
  
COPY privoxy.conf /etc/privoxy/config  
  
RUN chown -R privoxy /etc/privoxy  
  
USER privoxy  
  
ENTRYPOINT [ "privoxy", "--no-daemon" ]  
CMD [ "/etc/privoxy/config" ]  

