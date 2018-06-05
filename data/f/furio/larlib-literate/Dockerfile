# This docker file provides a build enviroment for larlib-literate  
FROM ubuntu:xenial  
  
# Tex and Pandoc  
RUN apt-get update -q && apt-get install -qy \  
texlive-full \  
python-pygments gnuplot \  
pandoc \  
make git wget \  
build-essential \  
&& rm -rf /var/lib/apt/lists/*  
  
# Nuweb  
RUN mkdir -p /usr/local/nuweb && cd /usr/local/nuweb \  
&& wget -q -O src.tar.gz https://storage.googleapis.com/google-code-archive-
downloads/v2/code.google.com/nuweb/nuweb-1.1.1-UWQSE.tar.gz \  
&& tar xzf src.tar.gz && ./configure && make && make install \  
&& cd && rm -fr /usr/local/nuweb \  
&& ln -s /usr/local/bin/nuweb /bin/nuweb  
  
# Julia 0.6  
RUN cd /usr/local && wget -q -O julia.tar.gz
https://julialang-s3.julialang.org/bin/linux/x64/0.6/julia-0.6.0-linux-x86_64.tar.gz
\  
&& tar xzf julia.tar.gz && rm julia.tar.gz \  
&& find . -maxdepth 1 -name 'julia-*' -exec bash -c 'mv $0 julia' {} \; \  
&& chmod +x /usr/local/julia/bin/julia && chmod +x /usr/local/julia/bin/julia-
debug \  
&& ln -s /usr/local/julia/bin/julia /usr/local/bin/julia \  
&& ln -s /usr/local/julia/bin/julia-dbg /usr/local/bin/julia-debug \  
&& julia -e 'Pkg.status()'  
  
WORKDIR /data  
VOLUME ["/data"]

