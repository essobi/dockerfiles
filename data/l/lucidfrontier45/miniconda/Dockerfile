FROM debian:jessie  
MAINTAINER Shiqiao Du <lucidfrontier.45@gmail.com>  
  
RUN set -ex \  
&& deps=' \  
bzip2 \  
ca-certificates \  
curl \  
libgomp1 \  
libgfortran3 \  
' \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $deps \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV PKG_URL https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh  
ENV INSTALLER miniconda.sh  
  
RUN set -ex \  
&& curl -kfSL $PKG_URL -o $INSTALLER \  
&& chmod 755 $INSTALLER \  
&& ./$INSTALLER -b -p /opt/conda3 \  
&& rm $INSTALLER  
  
ENV PATH /opt/conda3/bin:$PATH  

