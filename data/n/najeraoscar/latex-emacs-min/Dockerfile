FROM ubuntu:latest  
  
MAINTAINER oscar  
  
RUN apt-get update && apt-get --no-install-recommends install -y \  
ca-certificates \  
biber \  
latexmk \  
make \  
texlive-bibtex-extra \  
texlive-fonts-recommended \  
texlive-fonts-extra \  
texlive-generic-recommended \  
texlive-latex-base \  
texlive-latex-extra \  
texlive-latex-recommended \  
texlive-publishers \  
texlive-science \  
cm-super \  
emacs \  
git \  
wget \  
unzip \  
&& apt-get clean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /data  
VOLUME ["data"]  
  
COPY install-org.el /tmp/  
RUN emacs --batch --load /tmp/install-org.el  

