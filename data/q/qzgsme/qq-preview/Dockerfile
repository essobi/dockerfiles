FROM alpine:latest  
MAINTAINER dev@qzgs.me  
  
COPY app/ /usr/src/app/  
  
RUN apk add --no-cache --update python3 \  
&& pip3 install -U pip \  
&& pip3 install -r /usr/src/app/requirements.txt \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /root/.cache/pip/*  
  
WORKDIR /usr/src/app/  
VOLUME /data  
  
ENTRYPOINT ["/usr/src/app/init.sh"]  
CMD ["./run.py"]  

