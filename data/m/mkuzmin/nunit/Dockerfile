FROM mono:4.6  
ARG VERSION_TAG=3.5  
ARG VERSION_NUMBER=3.5.0  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get -qq update \  
&& apt-get -y install wget ca-certificates unzip \  
&& wget https://github.com/nunit/nunit-
console/releases/download/$VERSION_TAG/NUnit.$VERSION_NUMBER.zip -O
/tmp/nunit.zip -nv \  
&& unzip -q /tmp/nunit.zip -d /opt/nunit-console/ \  
&& echo '#!/bin/sh\nmono /opt/nunit-console/nunit3-console.exe "$@"'
>/usr/local/bin/nunit3-console \  
&& chmod +x /usr/local/bin/nunit3-console \  
&& apt-get -y purge --auto-remove wget ca-certificates unzip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

