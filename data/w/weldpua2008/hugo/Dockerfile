FROM alpine:3.4  
MAINTAINER Valeriy Solovyov <weldpua2008@gmail.com>  
  
# example with jq  
# apk add --update curl jq  
# curl -L -H 'Accept: application/json'
https://api.github.com/repos/$GITHUB_REPO/releases/latest| jq '.assets[]
.browser_download_url'|grep -i linux|grep -i tar.gz|grep -i '64bit'  
RUN apk add --update curl git openssh-client && \  
echo "Installed dependencies" && \  
set -x && \  
export GITHUB_REPO="spf13/hugo" && \  
export LATEST_RELEASE=$(curl -L -s -H 'Accept: application/json'
https://github.com/$GITHUB_REPO/releases/latest) && \  
export LATEST_VERSION=$(echo $LATEST_RELEASE | sed -e $'s/,"/,\\\\\n"/g'|grep
tag_name| sed -e 's/.*"tag_name":"\\(.*\\)".*/\1/') && \  
export ARTIFACT_FILENAME="hugo_${LATEST_VERSION//v}_Linux-64bit.tar.gz" && \  
export
ARTIFACT_URL="https://github.com/$GITHUB_REPO/releases/download/$LATEST_VERSION/$ARTIFACT_FILENAME"
&& \  
echo "exported VARS" && \  
curl -L $ARTIFACT_URL | tar xvz -C /tmp && \  
mv /tmp/hugo_*/hugo_* /usr/local/bin/hugo && \  
rm -rf /tmp/hugo_* && \  
rm -rf /var/cache/apk/* && \  
mkdir -p /site && \  
echo "Adding user & group for Hugo" && \  
addgroup -Sg 1000 hugo && \  
adduser -SG hugo -u 1000 -h /site hugo  
  
  
ADD entrypoint.sh /  
VOLUME /site  
WORKDIR /site  
#when used as a base image add the current folder to /site folder (workdir)  
#ONBUILD ADD . /site  
EXPOSE 1313  
ENTRYPOINT ["/entrypoint.sh"]  

