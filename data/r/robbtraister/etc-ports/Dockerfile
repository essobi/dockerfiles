FROM robbtraister/base  
  
RUN apk add --update --no-cache \  
bash \  
nginx \  
&& rm -rf /var/cache/apk/* \  
&& nginx -v \  
&& chown -R ${USER}:${USER} /var/lib/nginx \  
&& mkdir -p \  
./logs \  
&& ln -sf /dev/stdout ./logs/access.log \  
&& ln -sf /dev/stdout ./logs/error.log  
  
ADD . ./  
  
RUN chown -R ${USER}:${USER} . \  
&& chmod u=rwX,go= -R .  
  
USER ${USER}  
  
VOLUME /workdir/src  
  
CMD ./watch.sh  

