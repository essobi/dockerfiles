FROM anapsix/alpine-java:7  
MAINTAINER Shiaupiau <stu43005@gmail.com>  
  
ENV HatH_PORT 11112  
RUN apk update && \  
apk --no-cache add curl sqlite unzip && \  
mkdir -p /hath && \  
cd /hath && \  
curl -fsSL https://repo.e-hentai.org/hath/HentaiAtHome_1.4.2.zip -o hath.zip
&& \  
echo -n "da25fdec0a9535b265677a230e5cf84c75f0cfe790cffc51a520cf7cf3b01b2f
hath.zip" | sha256sum -c && \  
unzip hath.zip && \  
rm hath.zip && \  
apk del curl unzip && \  
mkdir -p /hath/cache && \  
mkdir -p /hath/data && \  
mkdir -p /hath/download && \  
mkdir -p /hath/log && \  
mkdir -p /hath/temp  
  
ADD client/start.sh /hath/start.sh  
  
RUN chmod +x /hath/start.sh  
  
WORKDIR /hath  
EXPOSE "$HatH_PORT"  
VOLUME ["/hath/cache", "/hath/data", "/hath/download", "/hath/log",
"/hath/temp"]  
CMD ["/hath/start.sh"]  

