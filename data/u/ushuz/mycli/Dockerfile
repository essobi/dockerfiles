FROM python:alpine  
  
ARG MYCLI_VERSION=1.16.0  
RUN set -ex \  
&& apk add --no-cache less \  
&& apk add --no-cache --virtual .build-deps gcc musl-dev python3-dev libffi-
dev openssl-dev \  
&& pip install --no-cache-dir mycli==$MYCLI_VERSION \  
&& apk del --purge .build-deps  
  
ENTRYPOINT ["mycli"]  
  
CMD ["--help"]  

