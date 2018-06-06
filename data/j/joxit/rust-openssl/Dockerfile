# Copyright 2017 Jones Magloire @Joxit  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
FROM debian:jessie-slim  
LABEL maintainer "Jones Magloire @Joxit"  
  
WORKDIR /opt/rust  
  
ENV RUST_ARCHIVE=rust-1.24.1-x86_64-unknown-linux-gnu.tar.gz  
ENV RUST_DOWNLOAD_URL=https://static.rust-lang.org/dist/$RUST_ARCHIVE  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends ca-certificates wget gcc libssl-
dev libc6-dev \  
&& mkdir build \  
&& cd build \  
&& wget -q $RUST_DOWNLOAD_URL \  
&& wget -q -O - $RUST_DOWNLOAD_URL.sha256 | sha256sum -c - \  
&& tar -xzf $RUST_ARCHIVE \--strip-components=1 \  
&& ./install.sh \--without=rust-docs \  
&& cd /opt/rust \  
&& rm -r build \  
&& apt-get autoremove --purge -y wget ca-certificates \  
&& rm -rf /var/lib/apt/lists/*

