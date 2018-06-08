FROM vvakame/review:2.5  
# Setup and Install  
# * bzip2: for installing jlisting.sty  
# * imagemagick: convert images  
RUN apt-get update && \  
apt-get install -y \  
bzip2 \  
imagemagick && \  
apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
# Install jlisting.sty  
RUN mkdir -p /usr/share/texlive/texmf-dist/tex/latex/jlisting && \  
curl http://iij.dl.sourceforge.jp/mytexpert/26068/jlisting.sty.bz2 | \  
bunzip2 > /usr/share/texlive/texmf-dist/tex/latex/jlisting/jlisting.sty && \  
mktexlsr  
  
# Install kindlegen  
ENV KINDLEGEN_VERSION=kindlegen_linux_2.6_i386_v2_9  
RUN mkdir -p /tmp/kindlegen && \  
cd /tmp/kindlegen && \  
curl http://kindlegen.s3.amazonaws.com/${KINDLEGEN_VERSION}.tar.gz -o
kindlegen.tar.gz && \  
tar xvf kindlegen.tar.gz && \  
chown root. kindlegen && \  
chmod 755 kindlegen && \  
mv kindlegen /usr/local/bin/ && \  
rm -rf /tmp/kindlegen  

