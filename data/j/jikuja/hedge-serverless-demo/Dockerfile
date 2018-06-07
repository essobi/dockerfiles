FROM node:alpine  
  
ENV BOOT_AS_ROOT=yes  
WORKDIR /app  
EXPOSE 3000  
RUN apk add --no-cache bash curl git nano openjdk8 \  
&& cd /usr/local/bin && curl -fsSLo boot https://github.com/boot-clj/boot-
bin/releases/download/latest/boot.sh && chmod 755 boot  
RUN npm install -g serverless  
  
RUN git clone https://github.com/jikuja/hedge-example-aws.git \  
&& cd hedge-example-aws \  
&& mkdir resources || true \  
&& npm install  
  
RUN apk add --no-cache --virtual build-dependencies python2 pkgconfig
libsecret-dev make g++ \  
&& git clone https://github.com/jikuja/hedge-example-azure.git \  
&& cd hedge-example-azure \  
&& mkdir resources || true \  
&& npm install \  
&& apk del build-dependencies  
  
RUN cd hedge-example-aws && boot \  
&& cd .. && cd hedge-example-azure && boot  
  
CMD bash  

