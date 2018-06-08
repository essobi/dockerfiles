FROM haskell  
  
# install pandoc  
RUN cabal update &&\  
cabal install pandoc &&\  
# install latex packages \  
apt-get update -y &&\  
apt-get install -y \--no-install-recommends \  
texlive-latex-base \  
texlive-xetex latex-xcolor \  
texlive-math-extra \  
texlive-latex-extra \  
texlive-fonts-extra \  
texlive-bibtex-extra \  
texlive-lang-spanish \  
texlive-generic-extra \  
fontconfig \  
curl \  
python &&\  
curl https://bootstrap.pypa.io/get-pip.py > get-pip.py &&\  
python get-pip.py &&\  
cabal install pandoc-citeproc &&\  
pip install MarkdownPP &&\  
apt-get install -y \--no-install-recommends biber &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -rf ~/.cabal/packages/*  
  
COPY compile.sh /  
  
CMD /compile.sh  

