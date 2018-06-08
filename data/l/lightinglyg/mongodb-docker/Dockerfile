FROM lightinglyg/alpine-base:edge  
  
COPY run.sh /root  
  
RUN echo http://dl-4.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories && \  
apk add --no-cache mongodb && \  
rm /usr/bin/mongosniff /usr/bin/mongoperf \  
&& chmod +x /root/run.sh  
  
VOLUME /data/db  
EXPOSE 27017  
ENTRYPOINT [ "/root/run.sh" ]  
CMD [ "mongod" ]  

