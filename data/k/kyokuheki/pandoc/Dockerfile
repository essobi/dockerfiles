FROM ubuntu:rolling  
#FROM ubuntu:devel  
LABEL maintainer Kyokuheki <kyokuheki@gmail.com>  
  
# ubuntu:rolling tag points to the latest release  
# ubuntu:latest tag points to the "latest LTS"  
  
ENV LANG=C.UTF-8 \  
LC_ALL=C.UTF-8 \  
DEBIAN_FRONTEND=noninteractive \  
URL_PANDOC_DEB=https://github.com/jgm/pandoc/releases/download/2.1.3/pandoc-2.1.3-1-amd64.deb
\  
URL_NOTO_SANS=https://noto-
website-2.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip \  
URL_NOTO_SERIF=https://noto-
website-2.storage.googleapis.com/pkgs/NotoSerifCJKjp-hinted.zip  
  
# install texlive  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends \  
texlive \  
texlive-latex-base \  
texlive-latex-recommended \  
texlive-latex-extra \  
texlive-luatex \  
texlive-fonts-recommended \  
texlive-fonts-extra \  
texlive-generic-recommended \  
texlive-lang-japanese \  
lmodern \  
fonts-texgyre \  
ghostscript \  
unzip \  
wget \  
ca-certificates \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# install pandoc  
RUN set -x \  
&& wget -qO pandoc.deb --no-check-certificate $URL_PANDOC_DEB \  
&& dpkg -i pandoc.deb \  
&& rm pandoc.deb  
  
# install noto fonts  
RUN set -x \  
&& mkdir -p /usr/share/fonts/opentype/noto \  
&& wget -q $URL_NOTO_SANS $URL_NOTO_SERIF \  
&& unzip -ou ${URL_NOTO_SANS##*/} -d /usr/share/fonts/opentype/noto \  
&& unzip -ou ${URL_NOTO_SERIF##*/} -d /usr/share/fonts/opentype/noto \  
&& ln -sf /usr/share/fonts/opentype/noto/NotoSansCJKjp-Black.otf
/usr/share/fonts/opentype/noto/NotoSansCJKJPBlack.otf \  
&& ln -sf /usr/share/fonts/opentype/noto/NotoSansCJKjp-Bold.otf
/usr/share/fonts/opentype/noto/NotoSansCJKJPBold.otf \  
&& ln -sf /usr/share/fonts/opentype/noto/NotoSansCJKjp-DemiLight.otf
/usr/share/fonts/opentype/noto/NotoSansCJKJPDemiLight.otf \  
&& ln -sf /usr/share/fonts/opentype/noto/NotoSansCJKjp-Light.otf
/usr/share/fonts/opentype/noto/NotoSansCJKJPLight.otf \  
&& ln -sf /usr/share/fonts/opentype/noto/NotoSansCJKjp-Medium.otf
/usr/share/fonts/opentype/noto/NotoSansCJKJPMedium.otf \  
&& ln -sf /usr/share/fonts/opentype/noto/NotoSansCJKjp-Regular.otf
/usr/share/fonts/opentype/noto/NotoSansCJKJPRegular.otf \  
&& ln -sf /usr/share/fonts/opentype/noto/NotoSansCJKjp-Thin.otf
/usr/share/fonts/opentype/noto/NotoSansCJKJPThin.otf \  
&& ln -sf /usr/share/fonts/opentype/noto/NotoSerifCJKjp-Black.otf
/usr/share/fonts/opentype/noto/NotoSerifCJKJPBlack.otf \  
&& ln -sf /usr/share/fonts/opentype/noto/NotoSerifCJKjp-Bold.otf
/usr/share/fonts/opentype/noto/NotoSerifCJKJPBold.otf \  
&& ln -sf /usr/share/fonts/opentype/noto/NotoSerifCJKjp-ExtraLight.otf
/usr/share/fonts/opentype/noto/NotoSerifCJKJPExtraLight.otf \  
&& ln -sf /usr/share/fonts/opentype/noto/NotoSerifCJKjp-Light.otf
/usr/share/fonts/opentype/noto/NotoSerifCJKJPLight.otf \  
&& ln -sf /usr/share/fonts/opentype/noto/NotoSerifCJKjp-Medium.otf
/usr/share/fonts/opentype/noto/NotoSerifCJKJPMedium.otf \  
&& ln -sf /usr/share/fonts/opentype/noto/NotoSerifCJKjp-Regular.otf
/usr/share/fonts/opentype/noto/NotoSerifCJKJPRegular.otf \  
&& ln -sf /usr/share/fonts/opentype/noto/NotoSerifCJKjp-SemiBold.otf
/usr/share/fonts/opentype/noto/NotoSerifCJKJPSemiBold.otf \  
&& rm -rf ${URL_NOTO_SANS##*/} ${URL_NOTO_SERIF##*/}  
  
# install inconsolata  
RUN set -x \  
&& mkdir -p /usr/share/texlive/texmf-dist/fonts/opentype/public/inconsolata \  
&& wget -qO /usr/share/texlive/texmf-
dist/fonts/opentype/public/inconsolata/Inconsolatazi4-Bold.otf
http://mirrors.ctan.org/fonts/inconsolata/opentype/Inconsolatazi4-Bold.otf \  
&& wget -qO /usr/share/texlive/texmf-
dist/fonts/opentype/public/inconsolata/Inconsolatazi4-Regular.otf
http://mirrors.ctan.org/fonts/inconsolata/opentype/Inconsolatazi4-Regular.otf  
  
RUN set -x \  
&& mktexlsr \  
&& luaotfload-tool -vvv --update --force \  
&& luaotfload-tool \--list=* --fields=plainname  
  
VOLUME ["/src"]  
WORKDIR /src  
  
ENTRYPOINT ["/usr/bin/pandoc", \  
"-o", "output.pdf", \  
"-s", "--verbose", \  
"--from", "markdown_github+raw_tex", \  
"--pdf-engine=lualatex", \  
"-N", "--toc", "--toc-depth=2", \  
"-V", "documentclass=ltjsarticle", \  
"-V", "geometry:margin=3cm", \  
"-V", "papersize=a4", \  
"-V", "luatexjapresetoptions=noto-otf", \  
"-V", "mainfont=TeX Gyre Termes", "-V",
"mainfontoptions=Ligatures=TeX,Scale=0.95", \  
"-V", "sansfont=TeX Gyre Heros", "-V",
"sansfontoptions=Ligatures=TeX,Scale=0.95", \  
"-V", "monofont=Inconsolatazi4" \  
]  

