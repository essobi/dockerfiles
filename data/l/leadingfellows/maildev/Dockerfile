FROM djfarrelly/maildev  
  
USER root  
RUN set -xe && \  
apk add \--update --no-cache \  
bash  
  
ENV MAILDEV_PORT=1025  
ENV MAILDEV_HTTP_PORT=8025  
COPY ./docker-entrypoint.sh /usr/local/bin/  
  
RUN adduser -D -u 1001 maildev  
RUN chown -R maildev /usr/src/app/  
USER maildev  
  
WORKDIR /usr/src/app/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["/usr/src/app/bin/maildev"]  

