FROM apluslms/grading-base:2.1  
RUN apt-get update -qqy && DEBIAN_FRONTEND=noninteractive apt-get install -qqy
--no-install-recommends \  
-o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" \  
bc \  
pdf2svg \  
texlive-fonts-recommended \  
texlive-games \  
texlive-latex-base \  
texlive-latex-extra \  
texlive-pictures \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
ARG VERSION=5.2.2  
ARG FILE=clingo-$VERSION-linux-x86_64  
  
RUN cd /usr/local/bin/ \  
&& curl -LSs
https://github.com/potassco/clingo/releases/download/v$VERSION/$FILE.tar.gz -o
- \  
| tar -zx --strip-components=1 \  
$FILE/clasp \  
$FILE/clingo \  
$FILE/gringo \  
$FILE/lpconvert \  
$FILE/reify  

