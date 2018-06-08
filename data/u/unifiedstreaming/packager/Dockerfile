FROM alpine:3.4  
LABEL maintainer "Unified Streaming <support@unified-streaming.com>"  
  
# Install packages  
RUN wget -q -O /etc/apk/keys/alpine@unified-streaming.com.rsa.pub \  
http://apk.unified-streaming.com/alpine@unified-streaming.com.rsa.pub  
  
RUN apk --update \  
\--repository http://apk.unified-streaming.com/repo \  
add mp4split=1.8.4-r0  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  
CMD ["--help"]  

