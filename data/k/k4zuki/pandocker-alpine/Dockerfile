FROM alpine:3.6  
MAINTAINER k4zuki  
  
RUN apk --no-cache add -U make librsvg curl openssl gcc libc-dev libc6-compat
openjdk8 graphviz && \  
mkdir -p /workdir && \  
mkdir -p /usr/local/share/fonts  
COPY src/sourcecodepro/*.ttf /usr/local/share/fonts/  
COPY src/sourcesanspro/*.ttf /usr/local/share/fonts/  
COPY bin/pandoc-crossref-alpine /usr/local/bin/pandoc-crossref  
  
WORKDIR /workdir  
  
RUN apk --no-cache add -U python3 py3-pillow libxml2-dev libxslt-dev
python3-dev \  
musl-dev bash git  
  
# dependencies for texlive  
RUN apk --no-cache add -U --repository
http://dl-3.alpinelinux.org/alpine/v3.7/main \  
poppler harfbuzz-icu py3-libxml2 && \  
pip3 install \  
pantable csv2table \  
six pandoc-imagine \  
svgutils \  
pyyaml \  
git+https://github.com/K4zuki/wavedrompy.git \  
git+https://github.com/K4zuki/bitfieldpy.git \  
git+https://github.com/K4zuki/pandocker-filters.git \  
git+https://github.com/pandocker/removalnotes.git  
  
RUN wget -c
https://github.com/logological/gpp/releases/download/2.25/gpp-2.25.tar.bz2 &&
\  
tar jxf gpp-2.25.tar.bz2 && cd gpp-2.25 && ./configure && make && cp src/gpp
/usr/bin/  
  
RUN apk add openjdk8-jre fontconfig ttf-dejavu  
ENV PLANTUML_VERSION 1.2017.18  
ENV PLANTUML_DOWNLOAD_URL
https://sourceforge.net/projects/plantuml/files/plantuml.$PLANTUML_VERSION.jar/download  
RUN curl -fsSL "$PLANTUML_DOWNLOAD_URL" -o /usr/local/plantuml.jar && \  
echo "#!/bin/bash" > /usr/local/bin/plantuml && \  
echo "java -jar /usr/local/plantuml.jar -Djava.awt.headless=true \$@" >>
/usr/local/bin/plantuml && \  
chmod +x /usr/local/bin/plantuml && plantuml -v  
  
ENV PANDOC_VERSION 2.1.3  
ENV PANDOC_ARCHIVE pandoc-$PANDOC_VERSION  
ENV PANDOC_URL
https://github.com/jgm/pandoc/releases/download/$PANDOC_VERSION/  
RUN wget --no-check-certificate $PANDOC_URL/$PANDOC_ARCHIVE-linux.tar.gz && \  
tar zxf $PANDOC_ARCHIVE-linux.tar.gz && cp $PANDOC_ARCHIVE/bin/*
/usr/local/bin/  
  
# ENV CROSSREF_VERSION v0.3.0.0  
# ENV CROSSREF_ARCHIVE linux-ghc8-pandoc-2-0.tar.gz  
# ENV CROSSREF_URL https://github.com/lierdakil/pandoc-
crossref/releases/download/$CROSSREF_VERSION  
# # RUN cabal update && cabal install pandoc-cross  
# RUN wget --no-check-certificate $CROSSREF_URL/$CROSSREF_ARCHIVE && \  
# tar zxf $CROSSREF_ARCHIVE && \  
# mv pandoc-crossref /usr/local/bin/  
RUN wget -c
https://github.com/tcnksm/ghr/releases/download/v0.5.4/ghr_v0.5.4_linux_amd64.zip
&& \  
unzip ghr_v0.5.4_linux_amd64.zip && \  
mv ghr /usr/local/bin/ && \  
rm ghr_v0.5.4_linux_amd64.zip  
  
RUN apk del *-doc  
  
WORKDIR /workdir  
  
VOLUME ["/workdir"]  
  
ENV TZ JST-9  
CMD ["bash"]  

