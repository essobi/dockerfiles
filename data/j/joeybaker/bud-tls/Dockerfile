# bud-tls  
  
FROM node:6  
MAINTAINER Joey Baker <joey@byjoeybaker.com>  
ENV BUD_VERSION 4.0.3  
  
# Build bud from source  
# the npm install is borked https://github.com/indutny/bud/issues/57  
# make sure the package repository is up to date  
RUN apt-get update -qq \  
&& apt-get install build-essential net-tools -y \  
# pull down bud  
&& mkdir /opt/bud-install \  
&& cd /opt/bud-install \  
&& git clone --depth 1 https://github.com/indutny/bud \  
&& cd bud \  
&& git checkout v$BUD_VERSION \  
&& git submodule update --init --recursive \  
# build gyp, we need subversion to get it, so install and then remove  
&& git clone https://chromium.googlesource.com/external/gyp.git tools/gyp \  
# build bud  
&& ./gyp_bud \  
&& make -C out/ \  
# move bud into place  
&& mkdir -p /opt/bud/ \  
&& cp -rf out/Release/bud /opt/bud/ \  
# cleanup  
&& cd / \  
&& rm -rf /opt/bud-install \  
&& apt-get purge build-essential -y \  
&& apt-get autoremove -y  
  
# add a user for bud to run workers as  
RUN adduser \--system --shell=/bin/bash \--group --gecos "" bud  
  
# install voxer's bud logger https://github.com/indutny/bud-logger  
# b/c the built in logger isn't so great, and @indutny suggested it  
RUN mkdir /opt/bud-logger-install \  
&& cd /opt/bud-logger-install \  
&& apt-get install build-essential -y \  
&& git clone --recursive git://github.com/indutny/bud-logger \  
&& cd bud-logger \  
&& ./gyp_logger \  
&& make -C out/ -j24 \  
&& cp -rf ./out/Release/logger.bud /opt/bud/ \  
# cleanup  
&& cd / \  
&& rm -rf /opt/bud-logger-install \  
&& apt-get purge build-essential -y \  
&& apt-get autoremove -y  
# Add `logger.bud` to the `tracing.dso` section in bud configuration  
  
# for some reason things break if using CMD, so we'll just have a script kick
off bud  
ADD ./start.sh /opt/bud/start.sh  
RUN chmod 770 /opt/bud/start.sh  
  
ENTRYPOINT ["/opt/bud/start.sh"]  
  
EXPOSE 443  

