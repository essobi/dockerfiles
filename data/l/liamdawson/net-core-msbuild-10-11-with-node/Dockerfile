FROM buildpack-deps:jessie-scm  
  
# Install .NET CLI dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libc6 \  
libcurl3 \  
libgcc1 \  
libgssapi-krb5-2 \  
libicu52 \  
liblttng-ust0 \  
libssl1.0.0 \  
libstdc++6 \  
libunwind8 \  
libuuid1 \  
zlib1g \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install .NET Core SDK 1.1  
ENV DOTNET_SDK_VERSION 1.0.0-preview2-1-003177  
ENV DOTNET_SDK_DOWNLOAD_URL
https://dotnetcli.blob.core.windows.net/dotnet/preview/Binaries/$DOTNET_SDK_VERSION/dotnet-
dev-debian-x64.$DOTNET_SDK_VERSION.tar.gz  
  
RUN curl -SL $DOTNET_SDK_DOWNLOAD_URL --output dotnet.tar.gz \  
&& mkdir -p /usr/share/dotnet \  
&& tar -zxf dotnet.tar.gz -C /usr/share/dotnet \  
&& rm dotnet.tar.gz \  
&& ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet  
  
# Install .NET Core runtime 1.0.3  
ENV STABLE_RUNTIME_VERSION 1.0.3  
ENV STABLE_RUNTIME_DOWNLOAD_URL https://go.microsoft.com/fwlink/?LinkID=836295  
  
RUN curl -SL $STABLE_RUNTIME_DOWNLOAD_URL --output dotnet.tar.gz \  
&& mkdir $STABLE_RUNTIME_VERSION \  
&& tar -xzf dotnet.tar.gz -C $STABLE_RUNTIME_VERSION \  
&& rm dotnet.tar.gz \  
&& cp -r $STABLE_RUNTIME_VERSION/host /usr/share/dotnet/ \  
&& cp -r $STABLE_RUNTIME_VERSION/shared /usr/share/dotnet/ \  
&& rm -rf $STABLE_RUNTIME_VERSION  
  
# Download node from the node dockerfile:  
  
RUN groupadd --gid 1000 node \  
&& useradd --uid 1000 \--gid node --shell /bin/bash --create-home node  
  
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
ENV NODE_VERSION 6.9.5  
  
RUN buildDeps='xz-utils' \  
&& set -x \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
\  
&& apt-get purge -y --auto-remove $buildDeps \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
# Trigger the population of the local package cache  
ENV NUGET_XMLDOC_MODE skip  
RUN mkdir warmup \  
&& cd warmup \  
&& dotnet new \  
&& cd .. \  
&& rm -rf warmup \  
&& rm -rf /tmp/NuGetScratch  
  
RUN npm i -g yarn

