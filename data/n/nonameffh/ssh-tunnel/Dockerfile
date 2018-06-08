FROM alpine:latest  
MAINTAINER Aleksey Tarasov <nonameffh@gmail.com>  
  
ENV LIST_HOST=127.0.0.1  
ENV LIST_PORT=1000  
ENV REMOTE_HOST=127.0.0.1  
ENV REMOTE_PORT=1000  
ENV KEY=/opt/ssh/id_rsa  
ENV ALIVE_COUNT=10  
ENV ALIVE_INTERVAL=60  
ENV ALIVE=yes  
ENV USERNAME=root  
ENV HOSTNAME=localhost  
  
RUN apk add --update openssh-client && rm -rf /var/cache/apk/* && mkdir /opt
&& mkdir /opt/ssh  
VOLUME /opt/ssh  
WORKDIR /opt/ssh  
  
COPY entrypoint.sh /  
COPY tunnel /bin/  
RUN chmod +x /entrypoint.sh && chmod +x /bin/tunnel  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["tunnel"]

