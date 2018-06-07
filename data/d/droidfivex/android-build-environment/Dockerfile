# Copyright 2018 droidfivex <droidfivex@gmail.com>  
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
FROM amd64/ubuntu:16.04  
LABEL maintainer="droidfivex <droidfivex@gmail.com>"  
  
RUN \  
apt-get update && \  
apt-get install -y \  
openjdk-8-jdk \  
git-core gnupg flex bison gperf build-essential zip curl zlib1g-dev gcc-
multilib g++-multilib libc6-dev-i386 lib32ncurses5-dev x11proto-core-dev
libx11-dev lib32z-dev ccache libgl1-mesa-dev libxml2-utils xsltproc unzip \  
python-minimal \  
curl && \  
curl http://commondatastorage.googleapis.com/git-repo-downloads/repo \  
-o /usr/local/bin/repo && \  
chmod a+x /usr/local/bin/repo  
  
# if you want to override this configuration, use '-e' option with 'docker
run'.  
# see https://docs.docker.com/engine/reference/run/#env-environment-variables  
ENV \  
GIT_AUTHOR_NAME="droidfivex" \  
GIT_AUTHOR_EMAIL="droidfivex@gmail.com" \  
GIT_COMMITTER_NAME="droidfivex" \  
GIT_COMMITTER_EMAIL="droidfivex@gmail.com" \  
GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no"  
RUN mkdir -p /workspace  
WORKDIR /workspace  
  
CMD ["bash"]  

