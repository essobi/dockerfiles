# Heavy NodeJS container  
  
FROM theferalrooster/nodejs-base:8.9.0  
USER root  
  
WORKDIR /srv/package  
  
RUN yum remove -y fakesystemd \  
&& rpm --rebuilddb \  
&& yum install -y \  
gcc.x86_64 \  
gcc-c++.x86_64 \  
make.x86_64 \  
bzip2.x86_64 \  
yum-plugin-ovl \  
git.x86_64 \  
krb5-devel.x86_64 \  
perl.x86_64 \  
python.x86_64 \  
ruby.x86_64 \  
ruby-devel.x86_64 \  
tree.x86_64 \  
zlib-devel.x86_64 \  
cyrus-sasl-devel.x86_64 \  
openssl-devel.x86_64 \  
libsecret-devel.x86_64 \  
libgnome-keyring-devel.x86_64 \  
&& yum clean all \  
&& npm install -g node-gyp node-pre-gyp prebuild  
  
# Install the nodejs source code for node-gyp  
COPY ./files/node-v8.9.0.tar.gz /tmp/  
  
RUN mkdir -p /usr/local/src/node \  
&& tar -xzf /tmp/node-v8.9.0.tar.gz \  
-C /usr/local/src/node \--strip-components=1 \  
&& rm -rf /tmp/*  

