FROM ubuntu:xenial  
MAINTAINER Daniel Krah <github@magdlos.com> ^  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -q \  
&& apt-get install -qy build-essential wget libfontconfig1 openjdk-9-jre
python-pygments \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install TexLive with scheme-basic  
RUN wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz; \  
mkdir /install-tl-unx; \  
tar -xvf install-tl-unx.tar.gz -C /install-tl-unx --strip-components=1; \  
echo "selected_scheme scheme-full" >> /install-tl-unx/texlive.profile; \  
/install-tl-unx/install-tl -profile /install-tl-unx/texlive.profile; \  
rm -r /install-tl-unx; \  
rm install-tl-unx.tar.gz; \  
find "/usr/local/texlive/2017/texmf-dist/doc/" -not -type d -delete  
  
ENV PATH="/usr/local/texlive/2017/bin/x86_64-linux:${PATH}"  
ENV HOME /data  
WORKDIR /data  
  
# Install latex packages  
RUN tlmgr install collection-basic && find "/usr/local/texlive/2017/texmf-
dist/doc/" -not -type d -delete  
RUN tlmgr install collection-bibtexextra && find
"/usr/local/texlive/2017/texmf-dist/doc/" -not -type d -delete  
RUN tlmgr install collection-binextra && find "/usr/local/texlive/2017/texmf-
dist/doc/" -not -type d -delete  
RUN tlmgr install collection-langenglish && find
"/usr/local/texlive/2017/texmf-dist/doc/" -not -type d -delete  
RUN tlmgr install collection-langgerman && find
"/usr/local/texlive/2017/texmf-dist/doc/" -not -type d -delete  
RUN tlmgr install collection-latex && find "/usr/local/texlive/2017/texmf-
dist/doc/" -not -type d -delete  
RUN tlmgr install collection-latexextra && find
"/usr/local/texlive/2017/texmf-dist/doc/" -not -type d -delete  
RUN tlmgr install collection-latexrecommended && find
"/usr/local/texlive/2017/texmf-dist/doc/" -not -type d -delete  
RUN tlmgr install collection-luatex && find "/usr/local/texlive/2017/texmf-
dist/doc/" -not -type d -delete  
RUN tlmgr install collection-mathscience && find
"/usr/local/texlive/2017/texmf-dist/doc/" -not -type d -delete  
RUN tlmgr install collection-pictures && find "/usr/local/texlive/2017/texmf-
dist/doc/" -not -type d -delete  
RUN tlmgr install collection-plaingeneric && find
"/usr/local/texlive/2017/texmf-dist/doc/" -not -type d -delete  
RUN tlmgr install collection-pstricks && find "/usr/local/texlive/2017/texmf-
dist/doc/" -not -type d -delete  
RUN rm -R /usr/local/texlive/2017/texmf-dist/doc/  
VOLUME ["/data"]  

