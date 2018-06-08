FROM ubuntu:16.04  
MAINTAINER MATSUI Shinsuke <poppen.jp@gmail.com>  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
texlive \  
texlive-lang-cjk \  
texlive-luatex \  
texlive-xetex \  
texlive-lang-japanese \  
lmodern \  
pandoc \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /src  
  
ENTRYPOINT ["pandoc"]  
CMD ["--help"]  

