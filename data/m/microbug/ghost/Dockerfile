FROM ghost:alpine  
  
RUN echo http://dl-2.alpinelinux.org/alpine/edge/community/ >>
/etc/apk/repositories \  
&& apk --no-cache add shadow  
  
ENV UID=1000  
ENV GID=1000  
COPY ./microbug-run.sh /microbug-run.sh  
  
ENTRYPOINT ["/microbug-run.sh"]  
CMD [""]  

