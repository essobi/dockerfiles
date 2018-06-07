FROM node:8-alpine  
  
ENV GLIBC_VERSION "2.27-r0"  
RUN apk add --no-cache python3 ca-certificates wget \  
&& wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub \  
&& wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk \  
&& apk add glibc-${GLIBC_VERSION}.apk \  
&& wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk \  
&& apk add glibc-bin-${GLIBC_VERSION}.apk \  
&& rm glibc-*.apk \  
&& apk del wget \  
&& if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi \  
&& if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3
/usr/bin/python; fi  
  
RUN pip install --upgrade pip pipenv awscli  
  
CMD ["/bin/sh"]  

