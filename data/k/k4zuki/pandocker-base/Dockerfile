FROM ubuntu:16.04  
  
MAINTAINER k4zuki  
  
ENV PLANTUML_VERSION 1.2017.18  
ENV PLANTUML_DOWNLOAD_URL
https://sourceforge.net/projects/plantuml/files/plantuml.$PLANTUML_VERSION.jar/download  
  
ENV PANDOC_VERSION 2.1.3  
ENV PANDOC_DOWNLOAD_URL
https://github.com/jgm/pandoc/releases/download/$PANDOC_VERSION/pandoc-$PANDOC_VERSION-1-amd64.deb  
ENV PANDOC_ROOT /usr/local/pandoc  
  
ENV LANG C.UTF-8  
  
RUN echo "deb http://ftp.jaist.ac.jp/pub/Linux/ubuntu/ xenial main restricted
universe multiverse" > /etc/apt/sources.list && \  
echo "deb http://ftp.jaist.ac.jp/pub/Linux/ubuntu/ xenial-updates main
restricted universe multiverse" >> /etc/apt/sources.list && \  
echo "deb http://ftp.jaist.ac.jp/pub/Linux/ubuntu/ xenial-security main
restricted universe multiverse" >> /etc/apt/sources.list && \  
apt-get -y update && \  
apt-get -y install wget curl unzip nano make ssh && \  
apt-get -y \--no-install-recommends install gpp \  
librsvg2-bin \  
git && \  
apt-get -y \--no-install-recommends install graphviz default-jre-headless && \  
curl -fsSL "$PLANTUML_DOWNLOAD_URL" -o /usr/local/bin/plantuml.jar && \  
echo "#!/bin/bash" > /usr/local/bin/plantuml && \  
echo "java -jar /usr/local/bin/plantuml.jar -Djava.awt.headless=true \$@" >>
/usr/local/bin/plantuml && \  
chmod +x /usr/local/bin/plantuml && \  
  
apt-get -y \--no-install-recommends install python3-pip python3-setuptools \  
python3-yaml \  
python3-six \  
python3-cairosvg && \  
pip3 install pantable csv2table \  
pandoc-imagine \  
svgutils && \  
  
wget -c $PANDOC_DOWNLOAD_URL && \  
dpkg -i pandoc-$PANDOC_VERSION-1-amd64.deb && \  
wget -c https://github.com/lierdakil/pandoc-
crossref/releases/download/v0.3.0.2/linux-ghc82-pandoc21.tar.gz && \  
tar zxf linux-ghc82-pandoc21.tar.gz && \  
mv pandoc-crossref /usr/local/bin/ && \  
  
# wget -c https://github.com/adobe-fonts/source-code-
pro/archive/2.030R-ro/1.050R-it.zip && \  
# unzip -e 1.050R-it.zip && cp source-code-
pro-2.030R-ro-1.050R-it/TTF/SourceCodePro-*.ttf /usr/local/share/fonts/ && \  
# wget -c https://github.com/adobe-fonts/source-sans-
pro/archive/2.020R-ro/1.075R-it.zip && \  
# unzip -e 1.075R-it.zip && cp source-sans-
pro-2.020R-ro-1.075R-it/TTF/SourceSansPro-*.ttf /usr/local/share/fonts/ && \  
# wget -c https://github.com/adobe-fonts/source-han-
sans/raw/release/OTF/SourceHanSansJ.zip && \  
# unzip -e SourceHanSansJ.zip && cp SourceHanSansJ/SourceHanSans-*.otf
/usr/local/share/fonts/ && \  
  
mkdir -p /workdir && \  
cd /workdir && \  
  
rm /pandoc-$PANDOC_VERSION-1-amd64.deb && \  
rm /linux*.gz && \  
rm -r ~/.cache/pip && \  
apt-get -y clean && \  
fc-cache -fv  
  
WORKDIR /workdir  
  
VOLUME ["/workdir"]  
  
CMD ["bash"]  

