FROM alpine:3.4  
RUN apk add -U tzdata  
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
COPY build/veincore /usr/bin/veincore  
  
ENV CORECONFIG_LISTEN_PORT 6888  
EXPOSE 6888  
CMD ["veincore"]  

