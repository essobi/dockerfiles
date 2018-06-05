# Copyright 2018 Akamai Technologies, Inc. All Rights Reserved.  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
#  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
FROM ubuntu  
  
# Base System  
ENV GOPATH="/goopt" PATH="${PATH}:/goopt/bin"  
RUN apt-get update && \  
apt-get install -y -q software-properties-common && \  
add-apt-repository -y ppa:longsleep/golang-backports && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y -q curl patch gawk g++ gcc
make libc6-dev patch libreadline6-dev zlib1g-dev libssl-dev libyaml-dev
libsqlite3-dev sqlite3 autoconf libgdbm-dev libncurses5-dev automake libtool
bison pkg-config libffi-dev software-properties-common nano jq libssl-dev
python-all wget vim python-pip php php-curl ruby-dev nodejs-dev npm php-pear
php-dev ruby perl golang-go git && \  
apt-get -qy autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
echo "alias gen_edgerc=/opt/examples/python/gen_edgerc.py" >> /root/.bashrc &&
\  
echo "alias verify_creds=/opt/examples/python/verify_creds.py" >>
/root/.bashrc && \  
echo "export PATH=${PATH}:/opt/bin" >> /root/.bashrc && \  
echo "cat /opt/container/MOTD" >> /root/.bashrc && \  
echo "PS1='DevOps World Tour [\w] >> '" >> /root/.bashrc  
# Akamai CLI / Terraform  
RUN mkdir /goopt && \  
go get github.com/akamai/cli && \  
cd /goopt/src/github.com/akamai/cli && \  
curl https://glide.sh/get | sh && \  
glide install && \  
go build -o akamai . && \  
mv akamai /usr/local/bin && \  
chmod 755 /usr/local/bin/akamai && \  
npm install -g n; n 7.0.0 && \  
/usr/local/bin/akamai install property purge netstorage auth && \  
rm -Rf /root/.akamai-cli/src/cli-*/release && \  
go get github.com/hashicorp/terraform && \  
go get github.com/akamai/AkamaiOPEN-edgegrid-golang && \  
go get github.com/xeipuuv/gojsonschema && \  
cd /goopt/src/github.com/hashicorp/terraform && \  
git remote add akamai https://github.com/dshafik/terraform.git && \  
git fetch \--all && \  
git checkout add-akamai-provider && \  
make quickdev && \  
mv /goopt/bin/terraform /usr/local/bin && \  
rm -Rf /goopt && \  
echo "ignore" > /root/.akamai-cli/.upgrade-check  
  
COPY . /opt  
# httpie  
RUN pip install httpie-edgegrid && \  
mkdir /root/.httpie && \  
cp /opt/container/config.json /root/.httpie/config.json  
# Libraries  
RUN cd /opt/php && \  
./composer.phar install && \  
cd /opt/ruby && \  
gem install bundler && \  
bundler install && \  
gem install akamai-edgegrid && \  
cd /opt/node && \  
npm install && \  
cd /opt/python && \  
python /opt/python/tools/setup.py install && \  
cpan -iT Akamai::Edgegrid LWP::Protocol::https  
  
WORKDIR "/opt"  
ENTRYPOINT ["/bin/bash"]  

