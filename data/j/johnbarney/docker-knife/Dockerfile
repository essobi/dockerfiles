FROM ruby:slim  
  
RUN mkdir -p /knife  
WORKDIR /knife  
VOLUME /knife  
RUN set -ex \  
&& buildDeps='libgmp3-dev gcc make' \  
&& apt update \  
&& apt upgrade -y \  
&& apt install -y --no-install-recommends $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& gem install chef \  
&& apt purge -y --auto-remove $buildDeps  
  
ENTRYPOINT ["knife"]  
CMD ["--help"]  

