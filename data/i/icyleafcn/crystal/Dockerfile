FROM icyleafcn/alpine:3.7  
LABEL maintainer="icyleaf <icyleaf.cn@gmail.com>"  
  
ENV CRYSTAL_VERSION=0.24.2-r1  
  
RUN echo http://public.portalier.com/alpine/testing >> /etc/apk/repositories
&& \  
wget
http://public.portalier.com/alpine/julien%40portalier.com-56dab02e.rsa.pub -O
/etc/apk/keys/julien@portalier.com-56dab02e.rsa.pub && \  
apk add --update --no-cache crystal=${CRYSTAL_VERSION} shards  
  
CMD ["crystal", "--version"]  

