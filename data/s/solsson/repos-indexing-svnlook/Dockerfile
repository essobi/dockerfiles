FROM
openjdk:8u121-jre@sha256:7c6b47748210f14f7905ce4e51dae53043a8535e119a4dfed8ae81766e5b03ec  
  
ENV reposIndexingStandaloneVersion=v1.1.2  
ENV reposIndexingStandaloneSourceUrl=https://github.com/Reposoft/repos-
indexing-standalone/archive/$reposIndexingStandaloneVersion.tar.gz  
ENV reposIndexingStandaloneSourceSha1=ffa9e2bbd76463fc7a201fcfdb7279a9bb1fe0e6  
  
RUN depsRuntime=' \  
' \  
&& depsBuild=' \  
openjdk-8-jdk-headless \  
maven \  
' \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $depsRuntime \  
&& apt-get install -y --no-install-recommends $depsBuild \  
&& rm -r /var/lib/apt/lists/* \  
&& curl -SLs "$reposIndexingStandaloneSourceUrl" -o repos-indexing-
standalone-$reposIndexingStandaloneVersion.tar.gz \  
&& echo "$reposIndexingStandaloneSourceSha1 repos-indexing-
standalone-$reposIndexingStandaloneVersion.tar.gz" | sha1sum -c - \  
&& mkdir -p usr/src/repos-indexing-standalone \  
&& tar -xvf repos-indexing-standalone-$reposIndexingStandaloneVersion.tar.gz
-C usr/src/repos-indexing-standalone --strip-components=1 \  
&& rm repos-indexing-* \  
&& cd usr/src/repos-indexing-standalone/ \  
&& mvn package \  
&& cd ../../../ \  
&& mv usr/src/repos-indexing-standalone/target/repos-indexing-standalone-jar-
with-dependencies.jar opt/repos-indexing-standalone-jar-with-dependencies.jar
\  
&& rm usr/src/repos-indexing-standalone -Rf \  
&& rm ~/.m2 -Rf \  
&& apt-get purge -y --auto-remove $depsBuild  
  
ENTRYPOINT [ "java", "-jar", "/opt/repos-indexing-standalone-jar-with-
dependencies.jar" ]  

