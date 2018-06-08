FROM openjdk:8u111-jre-alpine  
  
MAINTAINER SoftInstigate <info@softinstigate.com>  
  
ARG RELEASE  
  
RUN apk upgrade --update && apk add --update libstdc++ curl ca-certificates
bash  
  
WORKDIR /opt/  
  
RUN curl -sL
https://github.com/SoftInstigate/restheart/releases/download/${RELEASE}/restheart-${RELEASE}.tar.gz
--output restheart.tar.gz \  
&& tar -zxvf restheart.tar.gz \  
&& mv restheart-${RELEASE} restheart \  
&& rm -f restheart.tar.gz  
  
WORKDIR /opt/restheart  
COPY etc/* /opt/restheart/etc/  
COPY entrypoint.sh /opt/restheart/  
  
ENTRYPOINT ["./entrypoint.sh"]  
CMD ["etc/restheart.yml"]  
EXPOSE 8080 4443  

