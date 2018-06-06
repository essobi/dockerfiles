FROM alpine  
  
MAINTAINER Tatsuya Kitagawa <tatsuya.kitagawa@t13a.com>  
  
RUN apk add --no-cache \  
bash \  
coreutils \  
curl \  
openssh  
  
COPY absync-controller /absync-controller  
  
CMD [ "/usr/sbin/crond", "-f" ]  

