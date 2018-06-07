FROM alpine  
  
#Install packages  
RUN apk update \  
&& apk add gcc g++ libuv make python git && rm -rf /var/cache/apk/*  
  
#Install vanilla gyp because that's how I learned to compile C  
RUN cd /tmp && curl https://bootstrap.pypa.io/ez_setup.py -o - | python \  
&& git clone https://chromium.googlesource.com/external/gyp.git \  
&& cd gyp \  
&& python setup.py install \  
&& cd .. \  
&& rm -rf gyp  
  
#Clean up  
RUN cd /tmp \  
&& rm -rf apk \  
&& apk del git

