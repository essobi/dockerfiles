FROM node:boron  
  
RUN cd /usr/local && \  
curl -sL https://nodejs.org/download/release/$(node -v)/node-$(node
-v)-linux-x64.tar.xz \  
| tar -tJ \  
| sed -n 's/^[^/]*\/\(.*[^/]\)$/\1/p'\  
| xargs rm  
  
RUN nsolidver=$( \  
curl -sL https://nsolid-download.nodesource.com/download/metadata.json \  
| grep '^\s*"[0-9\.]*"' \  
| head -1 \  
| sed -n 's/.*"\([0-9\\.]*\)".*/\1/p' \  
) bash -c ' \  
curl -sL https://s3-us-west-2.amazonaws.com/nodesource-public-
downloads/${nsolidver}/artifacts/bundles/nsolid-
bundle-v${nsolidver}-linux-x64/nsolid-v${nsolidver}-boron-linux-x64.tar.gz \  
| tar xz --strip=1 -C /usr/local \  
'  

