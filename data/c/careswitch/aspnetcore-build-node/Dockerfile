FROM microsoft/dotnet:2.1-sdk  
  
# Set up Node  
# See https://nodejs.org/dist/v8.11.1/SHASUMS256.txt.asc  
ENV NODE_VERSION 8.11.1  
ENV NODE_DOWNLOAD_URL
https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz  
ENV NODE_DOWNLOAD_SHA
0e20787e2eda4cc31336d8327556ebc7417e8ee0a6ba0de96a09b0ec2b841f60  
  
RUN curl -SL "$NODE_DOWNLOAD_URL" \--output nodejs.tar.gz \  
&& echo "$NODE_DOWNLOAD_SHA nodejs.tar.gz" | sha256sum -c - \  
&& tar -xzf "nodejs.tar.gz" -C /usr/local \--strip-components=1 \  
&& rm nodejs.tar.gz \  
&& ln -sf /usr/local/bin/node /usr/local/bin/nodejs  
  

