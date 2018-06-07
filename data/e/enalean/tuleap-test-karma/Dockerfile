FROM ubuntu:18.04  
  
# Remove tag version for chromium-browser and the dep package chromium-codecs-
ffmpeg-extra  
# once https://bugs.chromium.org/p/chromium/issues/detail?id=829884 is fixed  
RUN apt-get update -y \  
&& apt-get install -y --no-install-recommends \  
nodejs \  
npm \  
git \  
chromium-browser=65.0.3325.181-0ubuntu1 \  
chromium-codecs-ffmpeg-extra=65.0.3325.181-0ubuntu1 \  
ca-certificates \  
&& apt-get clean \  
&& npm install --global npm@6.1.0 \  
&& npm config set progress false  
# This is used by bower to disable interactive mode  
ENV CI true  
  
COPY run.sh /run.sh  
  
VOLUME ["/sources"]  
  
RUN groupadd -r test-runner && useradd --create-home -r -g test-runner test-
runner \  
&& mkdir /output && chown -R test-runner:test-runner /output  
  
USER test-runner  
  
ENTRYPOINT ["/run.sh"]  

