FROM fedora  
  
MAINTAINER Dmitry Ustalov <dmitry.ustalov@gmail.com>  
  
RUN dnf install -y texlive texlive-collection-langcyrillic texlive-cm-unicode
texlive-polyglossia latexmk && dnf clean all  
  
WORKDIR /srv  

