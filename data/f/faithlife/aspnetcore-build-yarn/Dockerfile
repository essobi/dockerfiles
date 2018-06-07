FROM microsoft/dotnet:2.0.5-sdk-2.1.4-jessie  
# set up environment  
ENV ASPNETCORE_URLS http://+:80  
ENV ASPNETCORE_PKG_VERSION 2.0.5  
  
# set up node  
ENV NODE_VERSION 8.9.4  
ENV NODE_DOWNLOAD_URL
https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz  
ENV NODE_DOWNLOAD_SHA
21fb4690e349f82d708ae766def01d7fec1b085ce1f5ab30d9bda8ee126ca8fc  
  
RUN curl -SL "$NODE_DOWNLOAD_URL" \--output nodejs.tar.gz \  
&& echo "$NODE_DOWNLOAD_SHA nodejs.tar.gz" | sha256sum -c - \  
&& tar -xzf "nodejs.tar.gz" -C /usr/local \--strip-components=1 \  
&& rm nodejs.tar.gz \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs \  
# set up bower and gulp  
&& npm install -g bower gulp \  
&& echo '{ "allow_root": true }' > /root/.bowerrc  
# set up yarn  
ENV YARN_VERSION 1.3.2  
  
RUN set -ex \  
&& for key in \  
6A010C5166006599AA17F08146C2130DFD2497F5 \  
; do \  
gpg \--keyserver pgp.mit.edu \--recv-keys "$key" || \  
gpg \--keyserver keyserver.pgp.com \--recv-keys "$key" || \  
gpg \--keyserver ha.pool.sks-keyservers.net \--recv-keys "$key" ; \  
done \  
&& curl -fSLO \--compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \  
&& curl -fSLO \--compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \  
&& gpg \--batch \--verify yarn-v$YARN_VERSION.tar.gz.asc
yarn-v$YARN_VERSION.tar.gz \  
&& mkdir -p /opt/yarn \  
&& tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn \--strip-components=1 \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg \  
&& rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz  
  
# warmup NuGet package cache  
COPY packagescache.csproj /tmp/warmup/  
RUN dotnet restore /tmp/warmup/packagescache.csproj \  
\--source https://api.nuget.org/v3/index.json \  
\--verbosity quiet \  
&& rm -rf /tmp/warmup/  
  
WORKDIR /

