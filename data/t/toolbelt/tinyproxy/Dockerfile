FROM alpine  
  
RUN apk --no-cache add tinyproxy \  
&& sed 's/^Allow /#Allow /' -i /etc/tinyproxy/tinyproxy.conf  
  
EXPOSE 8888  
ENTRYPOINT [ "/usr/sbin/tinyproxy", "-d" ]  

