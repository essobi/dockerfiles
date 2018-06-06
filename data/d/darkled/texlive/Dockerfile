FROM bitnami/minideb  
  
ENV PATH /usr/local/texlive/bin/x86_64-linux:$PATH  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
wget \  
curl \  
ca-certificates \  
perl \  
libfontconfig \  
fonts-linuxlibertine \  
fonts-font-awesome \  
gnupg \  
&& update-ca-certificates \  
# create a profile  
&& printf "%s\n" \  
"selected_scheme scheme-minimal" \  
"TEXDIR /usr/local/texlive" \  
"TEXMFHOME /usr/local/texlive/texmf-local" \  
"TEXMFLOCAL /usr/local/texlive/texmf-local" \  
"TEXMFCONFIG /usr/local/texlive/texmf-config" \  
"TEXMFSYSCONFIG /usr/local/texlive/texmf-config" \  
"TEXMFVAR /usr/local/texlive/texmf-var" \  
"TEXMFSYSVAR /usr/local/texlive/texmf-var" \  
"option_doc 0" \  
"option_src 0" \  
"portable 1" > texlive.profile \  
&& wget -nv -O install-tl.tar.gz
http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz \  
&& mkdir -p install-tl \  
&& tar -xzf install-tl.tar.gz -C install-tl --strip-components=1 \  
&& ./install-tl/install-tl --persistent-downloads --profile=texlive.profile \  
&& tlmgr install \  
collection-basic \  
collection-bibtexextra \  
collection-fontsrecommended \  
collection-langcyrillic \  
collection-latex \  
collection-latexextra \  
collection-latexrecommended \  
collection-xetex \  
latexmk \  
fontawesome \  
babel-german \  
# remove unused packages  
&& tlmgr remove --force montex cbfonts koma-script \  
# && apt-get remove --purge -y wget curl ca-certificates \  
# clean up all temporary files  
&& rm -rf install-tl.tar.gz install-tl texlive.profile \  
&& apt-get autoclean -y \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/apt/lists/*  

