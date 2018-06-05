FROM buildpack-deps:jessie-curl  
  
ENV ASPELL_SERVER ftp://ftp.gnu.org/gnu/aspell  
ENV ASPELL_VERSION 0.60.6.1  
ENV ASPELL_EN 2015.04.24-0  
  
RUN apt-get update && apt-get install -y --no-install-recommends build-
essential \  
  
&& curl -SLO "${ASPELL_SERVER}/aspell-${ASPELL_VERSION}.tar.gz" \  
&& curl -SLO "${ASPELL_SERVER}/dict/en/aspell6-en-${ASPELL_EN}.tar.bz2" \  
  
&& tar -xzf "/aspell-${ASPELL_VERSION}.tar.gz" \  
&& tar -xjf "/aspell6-en-${ASPELL_EN}.tar.bz2" \  
  
&& cd "/aspell-${ASPELL_VERSION}" \  
&& ./configure \  
&& make \  
&& make install \  
&& ldconfig \  
  
&& cd "/aspell6-en-${ASPELL_EN}" \  
&& ./configure \  
&& make \  
&& make install \  
  
&& rm -rf /aspell* /var/lib/apt/lists/*  
ENTRYPOINT ["aspell"]  

