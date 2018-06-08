FROM hrektts/ubuntu:16.04.20160923.1  
MAINTAINER mps299792458@gmail.com  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
texlive texlive-fonts-extra texlive-lang-cjk texlive-lang-japanese \  
texlive-latex-extra texlive-luatex texlive-xetex latexdiff \  
lmodern gnuplot \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN sh -c "TERM=xterm luaotfload-tool --update"  
  
WORKDIR /data  
VOLUME ["/data"]  

