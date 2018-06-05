FROM docker:stable-dind  
  
ENV LANG=C.UTF-8 \  
JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk \  
PATH=${PATH}:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
  
RUN set -x \  
&& apk add --no-cache \  
bash \  
curl \  
git \  
py-pip \  
openjdk8 \  
&& apk add -U --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing
aufs-util \  
&& pip install --no-cache-dir "docker-compose"  
  
COPY ./entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

