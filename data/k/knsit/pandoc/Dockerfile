FROM alpine:edge as build  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk add --update texlive-full texmf-dist ghostscript librsvg ttf-dejavu
libarchive-tools make git && \  
mkdir -p /tmp/packages/tex && \  
cd /tmp/packages/tex && \  
wget -qO- http://ctan.mirrors.hoobly.com/macros/latex/contrib/csquotes.zip |
bsdtar -xvf - && \  
wget -qO- http://ctan.mirrors.hoobly.com/macros/latex/contrib/mdframed.zip |
bsdtar -xvf - && \  
wget -qO- http://ctan.mirrors.hoobly.com/macros/latex/contrib/makecmds.zip |
bsdtar -xvf - && \  
wget -qO- http://ctan.mirrors.hoobly.com/macros/latex/contrib/filecontents.zip
| bsdtar -xvf - && \  
wget -qO- http://ctan.mirrors.hoobly.com/macros/latex/contrib/needspace.zip |
bsdtar -xvf - && \  
wget -qO- http://ctan.mirrors.hoobly.com/macros/latex/contrib/titlesec.zip |
bsdtar -xvf - && \  
wget -qO- http://ctan.mirrors.hoobly.com/macros/latex/contrib/titling.zip |
bsdtar -xvf - && \  
wget -qO- http://mirror.hmc.edu/ctan//fonts/psfonts/ly1.zip | bsdtar -xvf - &&
\  
wget http://mirrors.ctan.org/macros/latex/contrib/etoolbox/etoolbox.sty && \  
wget http://ctan.mirrors.hoobly.com/macros/latex/contrib/mweights/mweights.sty
&& \  
git clone https://github.com/silkeh/latex-sourcesanspro.git /tmp/sourcesanspro
&& \  
rm -rf /tmp/sourcesanspro/doc /tmp/sourcesanspro/.git && \  
mv /tmp/sourcesanspro/tex/* /tmp/packages/tex/ && \  
mv /tmp/sourcesanspro/fonts /tmp/packages/ && \  
cd /tmp && \  
wget -qO- http://mirrors.ctan.org/fonts/sourcecodepro.zip | bsdtar -xvf - && \  
mv sourcecodepro/tex/* /tmp/packages/tex && \  
mkdir -p /tmp/packages/fonts/tfm/sourcecodepro && \  
mkdir -p /tmp/packages/fonts/enc/dvips/sourcecodepro && \  
mkdir -p /tmp/packages/fonts/map/dvips/sourcecodepro && \  
mkdir -p /tmp/packages/fonts/opentype/sourcecodepro && \  
mkdir -p /tmp/packages/fonts/type1/sourcecodepro && \  
mkdir -p /tmp/packages/fonts/vf/sourcecodepro && \  
mv sourcecodepro/fonts/SourceCodePro*.tfm
/tmp/packages/fonts/tfm/sourcecodepro && \  
mv sourcecodepro/fonts/*.enc /tmp/packages/fonts/enc/dvips/sourcecodepro && \  
mv sourcecodepro/fonts/SourceCodePro.map
/tmp/packages/fonts/map/dvips/sourcecodepro && \  
mv sourcecodepro/fonts/SourceCodePro*.otf
/tmp/packages/fonts/opentype/sourcecodepro && \  
mv sourcecodepro/fonts/SourceCodePro*.pfb
/tmp/packages/fonts/type1/sourcecodepro && \  
mv sourcecodepro/fonts/SourceCodePro*.vf /tmp/packages/fonts/vf/sourcecodepro
&& \  
cd /tmp/packages/tex/makecmds/ && \  
latex makecmds.ins && \  
cd /tmp/packages/tex/mdframed/ && \  
make all && \  
cd /tmp/packages/tex/filecontents && \  
latex filecontents.ins && \  
cd /tmp/packages/tex/titling && \  
latex titling.ins  
  
FROM alpine:edge  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
ENV PANDOC_VERSION="2.2.1"  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Pandoc" \  
org.label-schema.description="Pandoc container including PDFLaTeX to build
PDFs from Markdown" \  
org.label-schema.url="https://github.com/kns-it/Docker-Pandoc" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/kns-it/Docker-Pandoc" \  
org.label-schema.vendor="KNS" \  
org.label-schema.version=$PANDOC_VERSION \  
org.label-schema.schema-version="1.0" \  
maintainer="sebastian.kurfer@kns-it.de"  
  
COPY --from=build /tmp/packages /usr/share/texmf-var  
  
RUN sed -i -e 's/v3\\.[0-9]*/edge/g' /etc/apk/repositories && \  
echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk add --update --no-cache texlive-full texmf-dist ghostscript librsvg ttf-
dejavu && \  
rm -rf /var/cache/apk/* && \  
wget -P /tmp
https://github.com/jgm/pandoc/releases/download/${PANDOC_VERSION}/pandoc-${PANDOC_VERSION}-linux.tar.gz
&& \  
tar -xf /tmp/pandoc-${PANDOC_VERSION}-linux.tar.gz -C /tmp && \  
mv /tmp/pandoc-${PANDOC_VERSION}/bin/* /usr/bin/ && \  
rm -rf /tmp/* && \  
adduser pandoc -D -s /bin/sh && \  
texhash /usr/share/texmf-var && \  
cd /usr/share/texmf-var/tex/needspace && \  
pdflatex needspace.tex && \  
mktexlsr && \  
texhash /usr/share/texmf-var  
  
CMD [ "/bin/sh" ]  
  
USER pandoc  
WORKDIR /home/pandoc  

