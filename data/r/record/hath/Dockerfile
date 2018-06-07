FROM openjdk:8-jre-alpine  
  
# Hentai@Home URL  
# https://repo.e-hentai.org/hath/HentaiAtHome_1.4.2.zip  
ARG HATH_VERSION=1.4.2  
ARG
HATH_SHA256=da25fdec0a9535b265677a230e5cf84c75f0cfe790cffc51a520cf7cf3b01b2f  
ENV HATH_PORT=48763  
RUN apk --no-cache add \  
sqlite \  
&& true && \  
true  
  
RUN apk --no-cache add \  
\--virtual helpers \  
curl \  
unzip \  
&& true && \  
curl -fsSL "https://repo.e-hentai.org/hath/HentaiAtHome_$HATH_VERSION.zip" -o
/tmp/hath.zip && \  
echo -n "$HATH_SHA256 /tmp/hath.zip" | sha256sum -c && \  
mkdir -p \  
/hath \  
/hath/cache \  
/hath/data \  
/hath/download \  
/hath/log \  
/hath/temp \  
&& true && \  
unzip /tmp/hath.zip -d /hath && \  
rm /tmp/hath.zip && \  
apk del helpers && \  
true  
  
ADD entry.sh /hath/entry.sh  
WORKDIR /hath  
EXPOSE "$HATH_PORT/tcp"  
EXPOSE "$HATH_PORT/udp"  
VOLUME ["/hath/cache", "/hath/data", "/hath/download", "/hath/log",
"/hath/temp"]  
ENTRYPOINT ["/hath/entry.sh"]  

