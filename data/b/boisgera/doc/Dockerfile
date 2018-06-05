FROM ubuntu:14.04  
MAINTAINER Sébastien Boisgérault <Sebastien.Boisgerault@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV PYTHON python python-pip python-scipy python-matplotlib python-scipy
python-pil  
ENV LATEX texlive texlive-latex-extra dvipng texlive-luatex texlive-xetex \  
texlive-lang-english texlive-lang-french texlive-humanities  
  
RUN apt-get update && \  
apt-get install -y $PYTHON && \  
apt-get install -y $LATEX && \  
apt-get install -y git && \  
apt-get install -y curl && \  
apt-get install -y zip && \  
apt-get install -y pdf2svg && \  
apt-get install -y imagemagick && \  
apt-get install -y fonts-inconsolata && \  
# install pandoc  
cd /tmp && \  
apt-get install -y libgmp10 && \  
curl -L
https://github.com/jgm/pandoc/releases/download/1.16.0.2/pandoc-1.16.0.2-1-amd64.deb
> pandoc.deb && \  
dpkg --install pandoc.deb && \  
# install pandoc-templates  
cd /tmp && \  
git clone https://github.com/boisgera/pandoc-templates.git && \  
cd pandoc-templates && \  
./install.sh && \  
# install eul-doc  
cd /tmp && \  
git clone https://github.com/boisgera/eul-doc.git && \  
cd eul-doc && \  
pip install --target=.lib --ignore-installed 'about>=5.1,<6' && \  
pip install . && \  
# install eul-style  
curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash - && \  
apt-get install -y nodejs && \  
cd /tmp && \  
git clone https://github.com/boisgera/eul-style.git && \  
cd eul-style && \  
npm install -g coffee-script && \  
./install && \  
# clean-up and exit  
rm -rf /var/lib/apt/lists/* && apt-get clean && apt-get autoremove && \  
true  
  

