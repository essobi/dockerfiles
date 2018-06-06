FROM docker.io/jangorecki/r-base-dev  
  
MAINTAINER Jan Gorecki j.gorecki@wit.edu.pl  
  
# install qpdf for R check  
RUN apt-get update -qq \  
&& apt-get install -y --no-install-recommends qpdf \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# install latex required for building sweave vignettes and pdf manual  
# https://github.com/rocker-org/hadleyverse/blob/master/Dockerfile  
RUN apt-get update -qq \  
&& apt-get install -y --no-install-recommends \  
aspell \  
aspell-en \  
ghostscript \  
imagemagick \  
lmodern \  
texlive-fonts-recommended \  
texlive-humanities \  
texlive-latex-extra \  
texinfo \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& cd /usr/share/texlive/texmf-dist \  
&& wget http://mirrors.ctan.org/install/fonts/inconsolata.tds.zip \  
&& unzip inconsolata.tds.zip \  
&& rm inconsolata.tds.zip \  
&& echo "Map zi4.map" >> /usr/share/texlive/texmf-dist/web2c/updmap.cfg \  
&& mktexlsr \  
&& updmap-sys  
  
# install pandoc required for building markdown vignettes  
RUN PANDOC_VERSION='1.13.1' \  
&& PANDOC_DIR="${HOME}/opt/pandoc" \  
&& PANDOC_URL="https://s3.amazonaws.com/rstudio-
buildtools/pandoc-${PANDOC_VERSION}.zip" \  
&& mkdir -p "${PANDOC_DIR}" \  
&& curl -o /tmp/pandoc-${PANDOC_VERSION}.zip ${PANDOC_URL} \  
&& unzip -j /tmp/pandoc-${PANDOC_VERSION}.zip
"pandoc-${PANDOC_VERSION}/linux/debian/x86_64/pandoc" -d "${PANDOC_DIR}" \  
&& chmod +x "${PANDOC_DIR}/pandoc" \  
&& ln -s "${PANDOC_DIR}/pandoc" /usr/local/bin \  
&& unzip -j /tmp/pandoc-${PANDOC_VERSION}.zip
"pandoc-${PANDOC_VERSION}/linux/debian/x86_64/pandoc-citeproc" -d
"${PANDOC_DIR}" \  
&& chmod +x "${PANDOC_DIR}/pandoc-citeproc" \  
&& ln -s "${PANDOC_DIR}/pandoc-citeproc" /usr/local/bin  
  
# start R  
CMD ["R"]  

