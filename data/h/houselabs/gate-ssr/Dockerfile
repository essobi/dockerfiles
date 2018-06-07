FROM houselabs/gate:latest  
MAINTAINER daxingplay <daxingplay@gmail.com>  
  
ADD src /  
  
ENV SSR_DEP git  
  
RUN set -ex \  
&& apk add --update $SSR_DEP python libsodium py-m2crypto \  
&& git clone -b manyuser https://github.com/breakwa11/shadowsocks.git \  
&& apk del --purge $SSR_DEP \  
&& rm -rf /var/cache/apk/*  
  
CMD ["/bin/bash", "/start.sh"]  

