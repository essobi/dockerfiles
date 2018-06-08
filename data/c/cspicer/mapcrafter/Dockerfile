FROM alpine:latest  
MAINTAINER Chris Spicer <git@cspicer.net>  
  
ENV CLIENT_VERSION 1.9.2  
ENV VERSION_MANIFEST_URL
https://launchermeta.mojang.com/mc/game/version_manifest.json  
  
RUN apk add \--no-cache \  
git \  
build-base \  
cmake \  
libpng-dev \  
libjpeg-turbo-dev \  
boost-dev \  
boost-iostreams \  
boost-system \  
boost-filesystem \  
boost-program_options \  
&& rm -rf /var/cache/apk/*  
  
RUN git clone \--depth 1 \  
https://github.com/mapcrafter/mapcrafter.git \  
/tmp/mapcrafter \  
&& cd /tmp/mapcrafter \  
&& cmake . \  
&& make install \  
&& rm -rf /tmp/mapcrafter  
# find minecraft client url and download to extract textures for mapcrafter  
RUN apk add \--no-cache \--virtual \  
build-deps \  
curl \  
jq \  
&& echo "## Retrieving minecraft version manifest..." \  
&& curl \--silent \  
\--show-error \  
\--location ${VERSION_MANIFEST_URL} \  
\--output /tmp/version_manifest.json \  
&& eval $(jq -r '.versions[] | select(.id|contains("'"$CLIENT_VERSION"'"))?| \  
{version: .url} | @sh "CLIENT_JSON_URL=\\(.version)"' \  
/tmp/version_manifest.json) \  
&& echo "## Retrieving minecraft client URL..." \  
&& curl \--silent \  
\--show-error \  
\--location "$CLIENT_JSON_URL" \  
\--output /tmp/client.json \  
&& eval $(jq -r '@sh "CLIENT_URL=\\(.downloads .client .url)"'
/tmp/client.json) \  
&& echo "## Retrieving minecraft client..." \  
&& curl \--silent \  
\--show-error \  
\--location "$CLIENT_URL" \  
\--output /tmp/client.jar \  
&& echo "## Extracting textures..." \  
&& mapcrafter_textures.py /tmp/client.jar /usr/local/share/mapcrafter/textures
\  
&& echo "## Cleaning up..." \  
&& apk del build-deps \  
&& rm /tmp/*.json /tmp/client.jar  
  
ENTRYPOINT ["mapcrafter"]  
CMD ["--help"]  

