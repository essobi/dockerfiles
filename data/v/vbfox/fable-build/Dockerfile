ARG ASPNET_VERSION=2.1.300  
FROM microsoft/dotnet:${ASPNET_VERSION}-sdk-stretch  
  
# Install Mono  
ARG MONO_VERSION=5.12.0.226  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& echo "deb http://download.mono-project.com/repo/debian stable-
stretch/snapshots/$MONO_VERSION main" > /etc/apt/sources.list.d/mono-official-
stable.list \  
&& cat /etc/apt/sources.list.d/mono-official-stable.list \  
&& apt-get update \  
&& apt-get install -y mono-runtime binutils curl mono-devel ca-certificates-
mono fsharp mono-vbnc nuget referenceassemblies-pcl \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
# Install Yarn  
ARG YARN_VERSION=1.7.0  
RUN set -ex \  
&& for key in \  
E21930C4D0A4AA4618581F7AE074D16EB6FF4DE3 \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \  
&& gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc
yarn-v$YARN_VERSION.tar.gz \  
&& mkdir -p /opt/yarn \  
&& tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn --strip-components=1 \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg \  
&& rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz  
  
CMD ["bash"]

