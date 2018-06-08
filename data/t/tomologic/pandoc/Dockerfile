FROM ubuntu:16.04  
# Set the env variables to non-interactive  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBIAN_PRIORITY critical  
ENV DEBCONF_NOWARNINGS yes  
  
RUN apt-get update -y \  
&& apt-get install -y --no-install-recommends \  
wget \  
texlive-latex-base \  
texlive-xetex latex-xcolor \  
texlive-math-extra \  
texlive-latex-extra \  
texlive-fonts-extra \  
texlive-bibtex-extra \  
texlive-fonts-recommended \  
fontconfig \  
transfig \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget --no-check-certificate
https://github.com/jgm/pandoc/releases/download/1.17.0.2/pandoc-1.17.0.2-1-amd64.deb
&& \  
dpkg -i pandoc* && \  
rm pandoc* && \  
apt-get clean  
  
RUN mkdir /source  
WORKDIR /source  
  
CMD ["pandoc", "--help"]  

