FROM eviles/alpine-sshd  
  
RUN apk --update add openssl nginx \  
&& apk add \--no-cache --virtual=.build-dependencies gcc python-dev musl-dev
libffi-dev openssl-dev \  
&& pip install certbot \  
&& apk del .build-dependencies \  
&& rm -rf /var/cache/apk/* \  
&& echo "[program:nginx]" >> /etc/supervisord.conf \  
&& echo "command=/run_nginx.sh" >> /etc/supervisord.conf \  
&& echo "stdout_logfile=/dev/stdout" >> /etc/supervisord.conf \  
&& echo "stdout_logfile_maxbytes=0" >> /etc/supervisord.conf \  
&& echo "stderr_logfile=/dev/stderr" >> /etc/supervisord.conf \  
&& echo "stderr_logfile_maxbytes=0" >> /etc/supervisord.conf \  
&& sed -i 's/ssl_session_cache/#ssl_session_cache/g' /etc/nginx/nginx.conf  
  
ADD default.conf.template /etc/nginx/default.conf.template  
ADD ssl.conf.template /etc/nginx/ssl.conf.template  
ADD run_nginx.sh /run_nginx.sh  
RUN chmod 755 /run_nginx.sh  
  
EXPOSE 80 443  

