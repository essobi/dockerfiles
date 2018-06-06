FROM alpine:edge  
  
ENV WORKERS 4  
ENV PIDFILE /tmp/sockd.pid  
ENV CFGFILE /etc/sockd.conf  
  
RUN apk add --no-cache --repository http://dl-
cdn.alpinelinux.org/alpine/edge/testing/ dante-server  
  
ADD sockd.conf /etc/sockd.conf  
  
EXPOSE 1080  
CMD sockd -f $CFGFILE -p $PIDFILE -N $WORKERS  

