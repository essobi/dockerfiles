FROM ubuntu:17.10  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && \  
apt-get --yes \--no-install-recommends --no-install-suggests install texlive
texlive-lang-english texlive-lang-german \  
texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-
generic-extra latexmk biber texlive-bibtex-extra texlive-science curl lmodern
dot2tex && \  
apt-get --yes install fonts-linuxlibertine fonts-inconsolata fonts-oflb-asana-
math git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD createFolders.sh /src/  
WORKDIR /src  

