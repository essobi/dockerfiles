FROM openjdk:7  
  
RUN apt-get update -y \  
&& apt-get install -y \  
ant \  
autoconf \  
automake \  
gawk \  
git \  
make \  
openssh-client \  
php5 \  
rsync \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
# Download and install Saxon 8  
RUN wget http://central.maven.org/maven2/net/sf/saxon/saxon/8.7/saxon-8.7.jar
\  
&& test "$( sha256sum saxon-8.7.jar | cut -d' ' -f1 )" =
211a67269e861723614700f379c77318609878fd2fc2fbd9c97420480334354c \  
&& mkdir -p /usr/share/ant/lib/saxon8/ \  
&& mv saxon-8.7.jar /usr/share/ant/lib/saxon8/saxon8.jar  
# Download and install Closure Compiler jar  
RUN wget http://dl.google.com/closure-compiler/compiler-20161201.tar.gz \  
&& test "$( sha256sum compiler-20161201.tar.gz | cut -d' ' -f1 )" =
240f3d1dbdaa4275fd234a01a3c875d2cb7ad5756147377a84247ce8a99ef3b3 \  
&& tar -xzvf compiler-20161201.tar.gz closure-compiler-v20161201.jar \  
&& mv -v closure-compiler-v20161201.jar /usr/share/ant/lib/closure-
compiler.jar \  
&& chown root:root /usr/share/ant/lib/closure-compiler.jar \  
&& chmod 0644 /usr/share/ant/lib/closure-compiler.jar \  
&& rm compiler-20161201.tar.gz  
  
# Install NodeJS/NPM  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 4.7.2  
  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
\  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
# Disable host key checking from within builds as we cannot interactively
accept them  
# TODO: It might be a better idea to bake ~/.ssh/known_hosts into the
container  
RUN mkdir -p ~/.ssh  
RUN printf "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config  

