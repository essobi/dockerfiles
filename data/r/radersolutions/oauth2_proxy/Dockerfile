FROM buildpack-deps:jessie-curl  
  
# set to 1 to use the failback values  
# set to 0 to attempt to pull the most-recent build  
ENV FAILBACK_OVERRIDE=0  
ENV oauth2Project=/bitly/oauth2_proxy  
  
  
# this group of ENV variables are backup in case the parsing doesnt work  
# we will also hard-code these when creating a historical branch  
# The values must match exactly the release from the $oauth2Project github
project  
ENV FAILBACK_OAUTH2_PROXY_BRANCH=v2.2  
ENV FAILBACK_OAUTH2_PROXY_VERSION=2.2.0  
ENV FAILBACK_GOLANG_VERSION=1.8.1  
ENV PATH /opt/oauth2-proxy/bin:$PATH  
  
RUN newArchive=`wget https://github.com$oauth2Project/releases/ -q -O - | grep
-m 1 "linux-amd64" | grep . -m $(( 1 - $FAILBACK_OVERRIDE )) | awk '{ print $2
}' | cut -d\" -f 2` && \  
if test "${newArchive#*"release"}" != "$newArchive" ; then export
ARCHIVE=$newArchive ; echo "ARCHIVE set to most-current oauth2_proxy release"
; else export
ARCHIVE=$oauth2Project/releases/download/$FAILBACK_OAUTH2_PROXY_BRANCH/oauth2_proxy-$FAILBACK_OAUTH2_PROXY_VERSION.linux-
amd64.go$FAILBACK_GOLANG_VERSION.tar.gz ; echo "ARCHIVE variable hardcoded
because dynamic method failed or was overridden" ; fi && \  
tarPath=https://github.com$ARCHIVE && \  
echo "Downloading $tarPath" ; mkdir -p /opt/oauth2-proxy/bin && mkdir
/opt/oauth2-proxy/etc && \  
curl -L -k --silent \  
$tarPath | \  
tar xz --strip-components 1 -C /opt/oauth2-proxy/bin  
  
CMD oauth2_proxy -config=/opt/oauth2-proxy/etc/config -proxy-prefix
"/rader_oauth2"  
  

