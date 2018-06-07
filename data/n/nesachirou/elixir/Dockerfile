FROM nesachirou/erlang:20  
  
ENV PATH=/root/elixir/bin:$PATH LANG=C.UTF-8  
  
RUN set -ex \  
&& apk update \  
&& apk add -t .fetch-deps curl unzip \  
&& cd /root \  
&& curl -L https://github.com/elixir-
lang/elixir/releases/download/v1.6.3/Precompiled.zip > Precompiled.zip \  
&& unzip Precompiled.zip -d elixir \  
&& mix do local.hex \--force, local.rebar \--force \  
&& rm Precompiled.zip \  
&& apk del \--purge .fetch-deps \  
&& rm -rf /var/cache/apk/*  
  
CMD ["iex"]  

