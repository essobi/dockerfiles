FROM mhart/alpine-node  
  
ADD run /  
ADD https://raw.githubusercontent.com/mvertes/dosu/0.1.0/dosu /sbin/  
  
RUN chmod +x /sbin/dosu && \  
echo http://dl-4.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
&& \  
apk add --no-cache mongodb make gcc g++ git python  
  
VOLUME /data/db  
EXPOSE 27017 28017  
ENTRYPOINT [ "/run" ]  
CMD [ "mongod" ]  

