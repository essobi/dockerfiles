from debian:stretch as builder  
  
run apt update && \  
apt install -y haxe sudo git curl wget gnupg2  
run curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
run apt install -y nodejs  
  
run haxelib setup /usr/share/haxelib/ && \  
haxelib --global install hmm && \  
haxelib --global run hmm setup && \  
git clone https://github.com/kurzdigital/git-cache-http-server /tmp/git-cache-
http-server && \  
cd /tmp/git-cache-http-server && \  
hmm install && \  
haxe build.hxml && \  
npm pack  
  
from node:alpine  
  
run apk add --no-cache git tini  
copy \--from=builder /tmp/git-cache-http-server/*tgz /tmp/  
run npm install -g /tmp/*tgz  
  
expose 8080  
volume ["/tmp/cache/git"]  
  
stopsignal SIGTERM  
  
entrypoint ["/sbin/tini", "--"]  
  
cmd ["git-cache-http-server", "--port", "8080", "--cache-dir",
"/tmp/cache/git"]  

