FROM alpine  
LABEL maintainer="matteo@voxbox.io"  
  
ENV GIT_SSL_NO_VERIFY=1  
ENV APP sipdump  
VOLUME /var/log/${APP}  
  
ARG DEVICE  
ENV DEVICE ${DEVICE:-eth0}  
  
WORKDIR /usr/src  
  
RUN apk add --update build-base git libpcap-dev && \  
git clone https://github.com/voxbox-io/${APP} && cd ${APP} && \  
cc pcapsipdump.cpp calltable.cpp -lpcap -lstdc++ -o ${APP} && \  
ln -s /usr/src/${APP}/${APP} /usr/bin/${APP} && \  
apk del build-base git && \  
apk add libgcc libstdc++ && \  
rm -rf /var/cache/apk/*  
  
CMD /usr/bin/${APP} -f -U -R none -p -i ${DEVICE} -d /var/log/${APP}  

