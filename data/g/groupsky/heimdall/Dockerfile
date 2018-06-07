FROM debian:7  
# persistent / runtime deps  
RUN apt-get update && apt-get install -y ca-certificates libusb-1.0-0 --no-
install-recommends && rm -r /var/lib/apt/lists/*  
  
ENV HEIMDALL_VERSION 1.4.0  
ENV HEIMDALL_FILENAME debian7-heimdall_1.4.0-0_amd64.deb  
ENV HEIMDALL_SHA256
f80d95ac96363dde5af886a6726afb60f3a64b24fdc5f93629d580229be78294  
  
RUN buildDeps=" \  
curl \  
" \  
&& set -x \  
&& echo "installing prerequisites" \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
&& echo "downloading heimdall ${HEIMDALL_VERSION}" \  
&& curl -fSL
"https://bitbucket.org/benjamin_dobell/heimdall/downloads/${HEIMDALL_FILENAME}"
-o "$HEIMDALL_FILENAME" \  
&& echo "$HEIMDALL_SHA256 *$HEIMDALL_FILENAME" | sha256sum -c - \  
&& echo "installing heimdall $HEIMDALL_VERSION" \  
&& dpkg -i $HEIMDALL_FILENAME \  
&& echo "cleaning up" \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false $buildDeps \  
&& rm $HEIMDALL_FILENAME  
  
CMD /usr/local/bin/heimdall  

