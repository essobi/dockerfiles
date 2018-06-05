FROM alpine:3.4  
MAINTAINER pheonyx <alexandre.nicolaie@gmail.com>  
  
# RUN apk add \--no-cache ca-certificates wget curl make && \  
# cd $(mktemp -d) && \  
# echo -e "#!/bin/sh\nsrcdir=$(pwd)" > build && \  
# wget https://raw.githubusercontent.com/hlandau/acme/master/_doc/APKBUILD -O-
>> build && \  
# echo -e 'apk add --no-cache $makedepends && prepare && build && package' >>
build && \  
# chmod +x build && ./build && \  
# rm $(pwd) -rf && cd /  
  
RUN apk add \--no-cache ca-certificates wget curl bash openssl && \  
cd $(mktemp -d) && \  
curl -s -H 'Accept: application/vnd.github.v3+json' \  
'https://api.github.com/repos/hlandau/acme/releases/latest' | \  
sed 's/^.*"tag_name": *"v\\([^"]*\\)".*$/\1/;tx;d;:x' > version && \  
wget -O - https://github.com/hlandau/acme/releases/download/v$(cat
version)/acmetool-v$(cat version)-linux_amd64.tar.gz | tar xzf - && \  
cp acmetool-v$(cat version)-linux_amd64/bin/acmetool /usr/bin/acmetool && \  
rm -rf $(pwd) && cd /  
  
ADD start.sh /  
ADD acmedocker /bin/  
ADD quickstart.yaml /etc/acmetool/  
  
RUN chmod +x start.sh /bin/acmedocker  
  
CMD ["/start.sh"]

