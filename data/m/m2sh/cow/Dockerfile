FROM alpine:latest  
  
RUN apk add --no-cache --virtual .persistent-deps \  
ca-certificates \  
curl bash  
  
ENV COW_VERSION 0.9.8  
RUN curl -sSL https://github.com/cyfdecyf/cow/releases/download/0.9.8/cow-
linux64-{$COW_VERSION}.gz -o /tmp/cow.gz  
  
RUN gunzip /tmp/cow.gz \  
&& chmod +x /tmp/cow \  
&& mv /tmp/cow /usr/local/bin/cow \  
&& rm -f /tmp/cow.gz \  
&& mkdir $HOME/.cow  
  
# replace english version of config (rc)  
RUN curl -L https://cdn.rawgit.com/cyfdecyf/cow/master/doc/sample-config/rc-en
> $HOME/.cow/rc  
  
COPY entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
EXPOSE 7777  
VOLUME $HOME/.cow/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["cow"]  

