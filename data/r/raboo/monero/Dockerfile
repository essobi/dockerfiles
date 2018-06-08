FROM frolvlad/alpine-glibc:latest  
MAINTAINER Elias Abacioglu  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod 0755 /entrypoint.sh  
  
VOLUME /root/.bitmonero  
  
WORKDIR /root/.bitmonero  
  
EXPOSE 18080/tcp 18081/tcp  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
RUN set -xe \  
&& echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories \  
&& apk add --no-cache curl coreutils \  
&& curl -L https://downloads.getmonero.org/cli/linux64 | tar --strip-
components=2 -C /usr/bin -jxvf -  

