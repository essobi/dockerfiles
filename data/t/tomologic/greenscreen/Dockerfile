FROM phusion/baseimage  
  
RUN apt-get update && \  
apt-get install -y nodejs npm && \  
ln -s /usr/bin/nodejs /usr/bin/node && \  
rm -rf /var/lib/apt/lists/*  
  
ENV GREENSCREEN_DOWNLOAD_SHA1=ea83efb024d66ef840f3173528937a7ace28de36 \  
GREENSCREEN_GITSHA=1095132ed66ccf0f8a787f84bff63068a2b48ac1 \  
GREENSCREEN_DOWNLOAD_URL=https://github.com/groupon/greenscreen/archive/1095132ed66ccf0f8a787f84bff63068a2b48ac1.zip  
  
RUN set -x; buildDeps='curl ca-certificates unzip'; \  
apt-get update && \  
apt-get install -y $buildDeps && \  
curl -sSL "$GREENSCREEN_DOWNLOAD_URL" -o greenscreen.zip && \  
echo "$GREENSCREEN_DOWNLOAD_SHA1 *greenscreen.zip" | sha1sum -c - && \  
unzip greenscreen.zip && \  
mv greenscreen-${GREENSCREEN_GITSHA} /srv/greenscreen && \  
rm greenscreen.zip && \  
apt-get purge -y --auto-remove $buildDeps && rm -rf /var/lib/apt/lists/*  
  
WORKDIR /srv/greenscreen  
RUN npm install  
  
ADD greenscreen.sh /etc/service/greenscreen/run  
  
EXPOSE 4994  

