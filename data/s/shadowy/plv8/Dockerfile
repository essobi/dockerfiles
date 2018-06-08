FROM postgres:10.3  
  
ENV PLV8_VERSION=2.1  
  
RUN buildDependencies="build-essential \  
ca-certificates \  
python \  
curl \  
git-core \  
postgresql-server-dev-$PG_MAJOR" \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends ${buildDependencies} \  
&& mkdir -p /tmp/build \  
&& echo "https://github.com/plv8/plv8/archive/r${PLV8_VERSION}.tar.gz" \  
&& curl -o /tmp/build/plv8-${PLV8_VERSION}.tar.gz -SL
"https://github.com/plv8/plv8/archive/r${PLV8_VERSION}.tar.gz" \  
&& cd /tmp/build \  
&& tar -xzf /tmp/build/plv8-${PLV8_VERSION}.tar.gz -C /tmp/build/ \  
&& cd /tmp/build/plv8-r${PLV8_VERSION} \  
&& make static \  
&& make install \  
&& strip /usr/lib/postgresql/${PG_MAJOR}/lib/plv8.so \  
&& cd / \  
&& apt-get clean \  
&& apt-get remove -y ${buildDependencies} \  
&& apt-get autoremove -y \  
&& rm -rf /tmp/build /var/lib/apt/lists/*

