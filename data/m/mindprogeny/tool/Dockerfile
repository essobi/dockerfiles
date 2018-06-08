FROM alpine:edge  
  
WORKDIR /root  
  
RUN apk --no-cache add bash curl jq ruby  
  
RUN curl -skL "$(curl -s https://api.github.com/repos/pivotal-
cf/om/releases/latest|jq --raw-output '.assets[] | .browser_download_url' |
grep linux | grep -v zip)" > /usr/bin/om-linux && chmod 755 /usr/bin/om-linux  
  
RUN curl -skL "$(curl -s https://api.github.com/repos/pivotal-cf/pivnet-
cli/releases/latest|jq --raw-output '.assets[] | .browser_download_url' | grep
linux | grep -v zip)" > /usr/bin/pivnet-cli && chmod 755 /usr/bin/pivnet-cli  
  
RUN curl -skL https://s3.amazonaws.com/bosh-cli-artifacts/bosh-
cli-2.0.48-linux-amd64 > /usr/local/bin/bosh2 && chmod 0755
/usr/local/bin/bosh2  
  
RUN curl -skL "$(curl -s
https://api.github.com/repos/mikefarah/yq/releases/latest|jq --raw-output
'.assets[] | .browser_download_url' | grep linux_amd64)" > /usr/bin/yq &&
chmod 755 /usr/bin/yq  
  
WORKDIR /tmp  
  
RUN curl -skL
"https://packages.cloudfoundry.org/stable?release=linux64-binary&source=github"
| tar -xz && mv cf /usr/bin/cf && rm *  
  
WORKDIR /root  

