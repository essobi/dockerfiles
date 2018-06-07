FROM odoku/geopython:3.6  
COPY stack-fix.c entrypoint.sh /  
RUN apk add --no-cache --update \  
tini \  
llvm-dev \  
llvm \  
clang \  
libpng-dev \  
freetype-dev \  
&& apk add --no-cache --virtual build-dep musl-dev linux-headers git make g++
linux-headers \  
&& gcc -shared -fPIC /stack-fix.c -o /stack-fix.so \  
&& apk del build-dep \  
&& rm -rf /var/cache/apk/*  
  
ADD provision.sh /tmp/provision.sh  
RUN /tmp/provision.sh  
  
ADD requirements.txt /tmp/requirements.txt  
RUN pip3 install -r /tmp/requirements.txt  
RUN rm -rf /tmp/*  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["python3"]  

