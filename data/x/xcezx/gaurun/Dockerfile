FROM debian:jessie  
MAINTAINER xcezx <main.xcezx@gmail.com>  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GAURUN_VERSION 0.9.0  
ENV GAURUN_SHA1 ab2aa080e48190fbf4792d928994cb66186925fd  
  
RUN buildDeps='wget' \  
&& set -x \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget -O gaurun.tar.gz
"https://github.com/mercari/gaurun/releases/download/v$GAURUN_VERSION/gaurun-
linux-amd64-$GAURUN_VERSION.tar.gz" \  
&& echo "$GAURUN_SHA1 gaurun.tar.gz" | sha1sum -c - \  
&& tar -xzf gaurun.tar.gz -C /usr/local/bin --strip-components=1 \  
&& rm gaurun.tar.gz \  
&& apt-get purge -y --auto-remove $buildDeps  
  
CMD ["/usr/local/bin/gaurun"]  

