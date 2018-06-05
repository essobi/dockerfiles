FROM alpine:edge  
LABEL maintainer "Ilya Glotov <contact@ilyaglotov.com>"  
  
RUN apk --update --no-cache add gmp-dev \  
mpfr-dev \  
mpc1-dev \  
python3 \  
python3-dev \  
py3-pip \  
openssl \  
\  
&& apk --no-cache --virtual .deps add build-base \  
libffi-dev \  
openssl-dev \  
\  
&& pip3 install cryptography \  
gmpy2 \  
\  
&& apk del .deps \  
&& rm -rf /root/.cache/pip /var/cache/apk/*  
  
RUN adduser -D robot  
  
COPY robot-detect /robot-detect  
  
USER robot  
  
ENTRYPOINT ["/robot-detect"]  

