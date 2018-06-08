# Copyright (c) ThoughtWorks Inc. All rights reserved.  
# Licensed under the MIT license. See LICENSE file in the project root for
details.  
FROM centos/ruby-23-centos7  
  
WORKDIR /gauge  
  
USER root  
  
RUN \  
wget -O /tmp/gauge.zip `curl -s
https://api.github.com/repos/getgauge/gauge/releases | grep
browser_download_url | grep 'linux.x86_64.zip' | head -n 1 | cut -d '"' -f 4`
&& \  
unzip -d /tmp/gauge /tmp/gauge.zip && \  
cp /tmp/gauge/bin/gauge /usr/local/bin/ && \  
rm -rf /tmp/gauge /tmp/gauge.zip ~/.gauge/config ~/.gauge/logs && \  
chmod 777 /gauge  
  
USER default  
  
RUN gauge install ruby

