FROM dweomer/stunnel  
  
RUN apk add --update bash && \  
rm -rf /tmp/* /var/tmp/* /var/cache/apk/*  
  
ADD ./bin /usr/local/bin  
RUN chmod a+x /usr/local/bin/*  
  
ENTRYPOINT ["/bin/sh", "-c"]  
CMD ["pre_run"]  

