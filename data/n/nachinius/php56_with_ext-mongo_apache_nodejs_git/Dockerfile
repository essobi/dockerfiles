FROM nachinius/php56_with_ext-mongo_apache_nodejs  
  
MAINTAINER nachinius <ignacio.peixoto@gmail.com>  
  
#disable interactive  
ENV DEBIAN_FRONTEND noninteractive  
  
# install php mongodb extension  
RUN buildDeps="git" \  
&& set -x \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends &&
rm -rf /var/lib/apt/lists/*  

