FROM microsoft/dotnet:latest  
  
RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev  
  
#https://docs.docker.com/engine/installation/linux/debian/  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >
/etc/apt/sources.list.d/sources.list  
RUN apt-get update  
RUN apt-get update  
RUN apt-get install -y apt-transport-https ca-certificates  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D  
RUN echo "deb https://apt.dockerproject.org/repo debian-jessie main" >
/etc/apt/sources.list.d/docker.list  
RUN apt-get update  
RUN apt-cache policy docker-engine  
RUN apt-get install -y docker-engine  
#https://docs.docker.com/engine/installation/linux/debian/  
#https://github.com/nodejs/docker-
node/blob/dc9ceb77ad6d98258c825ee45aac219169bc3532/6.2/Dockerfile  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 6.2.2  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt  
#https://github.com/nodejs/docker-
node/blob/dc9ceb77ad6d98258c825ee45aac219169bc3532/6.2/Dockerfile  
COPY . /app  
WORKDIR /app  
RUN npm install && npm run build  
  
RUN ["dotnet", "restore"]  
  
RUN ["dotnet", "build"]  
  
RUN ["dotnet", "ef", "database", "update"]  
  
EXPOSE 5000/tcp  
  
ENTRYPOINT ["dotnet", "run", "--server.urls", "http://0.0.0.0:5000"]

