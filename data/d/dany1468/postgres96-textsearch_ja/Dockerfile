FROM postgres:9.6  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends ca-certificates wget build-
essential postgresql-server-dev-9.6 libmecab-dev mecab mecab-ipadic-utf8 \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget
https://github.com/oknj/textsearch_ja/archive/textsearch_ja-9.6.0.tar.gz \  
&& tar -xvzf textsearch_ja-9.6.0.tar.gz \  
&& rm textsearch_ja-9.6.0.tar.gz \  
&& cd textsearch_ja-textsearch_ja-9.6.0 \  
&& make USE_PGXS=1 \  
&& make USE_PGXS=1 install \  
&& cd ../ \  
&& rm -rf textsearch_ja-textsearch_ja-9.6.0 \  
&& apt-get purge -y \--auto-remove ca-certificates wget build-essential  
  

