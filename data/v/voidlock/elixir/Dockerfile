FROM voidlock/erlang:18.1  
  
ENV ELIXIR_VERSION=1.1.1 \  
ELIXIR_DOWNLOAD_SHA=3b7d6e4fdbcc82d19fa76f4e384f8a87535abcd00ef04528dc6b6706f32a106a  
  
RUN set -xe \  
&& curl -SL "https://github.com/elixir-
lang/elixir/archive/v${ELIXIR_VERSION}.tar.gz" -o elixir.tar.gz \  
&& echo "${ELIXIR_DOWNLOAD_SHA} elixir.tar.gz" | sha256sum -c - \  
&& mkdir -p /usr/src/elixir \  
&& tar -xzC /usr/src/elixir --strip-components=1 -f elixir.tar.gz \  
&& rm elixir.tar.gz \  
&& cd /usr/src/elixir \  
&& make -j$(nproc) clean install \  
&& rm -rf /usr/src/elixir  
  
CMD ["mix"]  

