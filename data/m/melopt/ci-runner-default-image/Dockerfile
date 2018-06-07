FROM ubuntu  
MAINTAINER Pedro Melo <melo@simplicidade.org>  
  
RUN apt-get update \  
&& apt-get install -y nodejs npm git docker.io carton redis-tools mysql-client
curl jq \  
&& ln -s /usr/bin/nodejs /usr/bin/node \  
&& npm install -g uglify-js csso gitbook-cli \  
&& cpanm -n App::cpanminus Carton Capture::Tiny Getopt::Long \  
&& apt-get clean autoclean \  
&& apt-get autoremove -y \  
&& rm -rf "$HOME/.cpanm" "$HOME/.npm"  
  
ENV MY_BINS /usr/local/bin  
  
RUN BASE="https://github.com/docker/compose" \  
&& LATEST_RELEASE=$(curl -L -s -H 'Accept: application/json'
"$BASE/releases/latest" | jq -r .tag_name) \  
&& echo "*** Installing docker-compose version $LATEST_RELEASE" \  
&& curl -L "$BASE/releases/download/$LATEST_RELEASE/docker-compose-
Linux-x86_64" \  
-o $MY_BINS/docker-compose \  
&& chmod +x $MY_BINS/docker-compose  
  
COPY cmd-retry docker-* ci-* $MY_BINS/  
RUN bash -c "chmod 555 $MY_BINS/{cmd-*,docker-*,ci-*}"  

