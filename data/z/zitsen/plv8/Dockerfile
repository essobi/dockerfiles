FROM postgres:9.5  
  
MAINTAINER Linhe Huo <linhe.huo@gmail.com>  
  
ENV PLV8_VERSION v2.0.3  
  
RUN buildDependencies="build-essential ca-certificates curl git-core
postgresql-server-dev-$PG_MAJOR python-pip" \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends ${buildDependencies} \  
&& mkdir -p /tmp/build \  
&& curl -o /tmp/build/${PLV8_VERSION}.tar.gz -SL
"https://github.com/plv8/plv8/archive/$PLV8_VERSION.tar.gz" \  
&& cd /tmp/build \  
&& tar -xzf /tmp/build/${PLV8_VERSION}.tar.gz -C /tmp/build/ \  
&& cd /tmp/build/plv8-${PLV8_VERSION#?} \  
&& make -j 4 static \  
&& make install \  
&& strip /usr/lib/postgresql/${PG_MAJOR}/lib/plv8.so \  
&& pip install pgxnclient \  
&& pgxn install pgTAP \  
&& apt-get clean \  
&& cd / \  
&& rm -rf /tmp/build /var/lib/apt/lists/*  

