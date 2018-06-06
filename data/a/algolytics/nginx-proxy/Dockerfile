FROM jwilder/nginx-proxy  
MAINTAINER Mikołaj Olszewski <mikolaj.olszewski@algolytics.pl>  
  
ENV ENTRYKIT_FILE=entrykit_0.4.0_Linux_x86_64.tgz  
  
COPY algo_proxy.conf.tmpl /etc/nginx/conf.d/  
ADD
https://github.com/progrium/entrykit/releases/download/v0.4.0/$ENTRYKIT_FILE
/tmp/  
RUN tar xzf /tmp/$ENTRYKIT_FILE -C /bin && rm -rf /tmp/$ENTRYKIT_FILE  
RUN entrykit --symlink  
  
ENTRYPOINT ["render", "/etc/nginx/conf.d/algo_proxy.conf", "--", "/app/docker-
entrypoint.sh"]  
CMD ["forego", "start", "-r"]  

