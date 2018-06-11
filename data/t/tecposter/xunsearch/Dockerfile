FROM tecposter/ubuntu:latest  
  
MAINTAINER "zhanjh@126.com"  
  
RUN set -ex \  
&& build_deps="wget bzip2 gcc g++ zlib1g-dev make" \  
&& apt-get update \  
&& apt-get upgrade --no-install-recommends --no-install-suggests -y \  
&& apt-get install $build_deps -y \  
  
&& cd /usr/local/src/ \  
&& wget http://www.xunsearch.com/download/xunsearch-full/xunsearch-
full-1.4.10.tar.bz2 \  
&& tar -xjf xunsearch-full-1.4.10.tar.bz2 \  
&& cd xunsearch-full-1.4.10 \  
&& sh ./setup.sh --prefix=/usr/local/xunsearch \  
  
&& echo '' >> /usr/local/xunsearch/bin/xs-ctl.sh \  
&& echo 'tail -f /dev/null' >> /usr/local/xunsearch/bin/xs-ctl.sh \  
  
&& cd / \  
&& rm -rf /usr/local/src/* \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge -y --auto-remove $build_deps  

