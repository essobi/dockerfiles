FROM robbtraister/watcher  
  
RUN apk add --update --no-cache \  
nginx \  
&& rm -rf /var/cache/apk/* \  
&& nginx -v \  
&& chown -R ${USER}:${USER} /var/lib/nginx \  
&& mkdir -p \  
./logs \  
&& ln -sf /dev/stdout ./logs/access.log \  
&& ln -sf /dev/stdout ./logs/error.log \  
&& chown -R ${USER}:${USER} . \  
&& chmod u=rwX,go= -R .  
  
ENV PROCESS="nginx" \  
ARGUMENTS="-p|../|-c|./nginx.conf|-g|daemon off; pid ./nginx.pid;"  
USER ${USER}  
  
WORKDIR ./src  
  
CMD ln -sf /workdir/src/* /workdir \  
&& cd /watcher \  
&& npm start  

