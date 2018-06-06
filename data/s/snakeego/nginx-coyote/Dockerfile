FROM nginx:stable-alpine  
  
ARG coyote_version=v1.2.0  
  
ADD
https://github.com/MagnaXSoftware/coyote/releases/download/${coyote_version}/coyote-
linux-amd64 /usr/local/bin/coyote  
ADD http://af.it-test.pw/su-exec/alpine/suexec /usr/local/bin/suexec  
COPY ./files/request.sh /usr/local/bin/certificate.sh  
  
RUN set -x \  
&& apk \--update --no-cache add openssl ca-certificates\  
&& chmod +x \  
/usr/local/bin/coyote \  
/usr/local/bin/suexec \  
/usr/local/bin/certificate.sh \  
&& adduser -HD -s /bin/false -G nginx -S coyote \  
&& mkdir \  
/cert \  
/etc/nginx/partial.d \  
/etc/coyote \  
/var/cache/coyote/ \  
&& openssl genrsa 4096 > /etc/coyote/account.key \  
&& chown coyote /etc/coyote/account.key \  
&& chmod 600 /etc/coyote/account.key \  
&& chown nginx:nginx /var/cache/coyote/ \  
&& chmod 770 /var/cache/coyote/  
  
COPY ./files/nginx.log.conf /etc/nginx/partial.d/log.conf  
COPY ./files/nginx.challenges.conf /etc/nginx/partial.d/challenges.conf  
COPY ./files/nginx.default.conf /etc/nginx/conf.d/default.conf  
COPY ./files/nginx.conf /etc/nginx/nginx.conf  
  
VOLUME /cert  

