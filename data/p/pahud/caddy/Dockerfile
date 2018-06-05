FROM abiosoft/caddy:php  
  
ENV ROOT_DIR /srv  
  
RUN rm -rf $ROOT_DIR/*  
ADD src $ROOT_DIR  
  
RUN apk -Uuv add bash groff less python py-pip && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/*  
  
ADD startup.sh /startup.sh  
RUN chmod a+x /startup.sh  
  
WORKDIR /srv  
  
EXPOSE 2015  
ENTRYPOINT []  
  
CMD ["/startup.sh"]  

