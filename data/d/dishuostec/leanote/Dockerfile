FROM alpine:3.7  
LABEL maintainer="dishuostec <dishuostec@gmail.com>"  
  
ARG ALPINE_REPO=http://dl-cdn.alpinelinux.org  
  
ENV LEANOTE_VERSION=2.6.1  
RUN ver=$(cat /etc/alpine-release | awk -F '.' '{printf "%s.%s", $1, $2;}') \  
&& repos=/etc/apk/repositories \  
&& mv -f ${repos} ${repos}_bk \  
&& echo "${ALPINE_REPO}/alpine/v${ver}/main" > ${repos} \  
&& echo "${ALPINE_REPO}/alpine/v${ver}/community" >> ${repos} \  
&& apk add --no-cache tzdata \  
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& echo Asia/Shanghai > /etc/timezone \  
\  
&& apk add --no-cache curl \  
&& curl -fsSL "https://sourceforge.net/projects/leanote-
bin/files/${LEANOTE_VERSION}/leanote-linux-
amd64-v${LEANOTE_VERSION}.bin.tar.gz/download" -o leanote.tar.gz \  
&& tar -xf leanote.tar.gz -C /usr/local \  
&& chmod +x /usr/local/leanote/bin/run.sh \  
&& apk del curl  
  
EXPOSE 9000  
WORKDIR /usr/local/leanote/bin  
ENTRYPOINT ["sh", "run.sh"]  
  

