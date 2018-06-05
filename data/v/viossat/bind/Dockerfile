FROM alpine:3.7  
MAINTAINER Mathieu Viossat <mathieu@viossat.fr>  
  
RUN apk add --no-cache bind \  
&& rm -rf /etc/bind /var/bind  
  
COPY config /etc/bind  
COPY run.sh /usr/local/bin/  
  
VOLUME /etc/bind /var/cache/bind  
  
EXPOSE 53 53/udp  
  
ENTRYPOINT ["run.sh"]  
CMD ["named", "-g", "-u", "named"]  

