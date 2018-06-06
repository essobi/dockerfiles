FROM debian:sid-slim  
  
RUN echo 'deb http://deb.debian.org/debian sid main contrib non-free' >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y install latex2html latex2rtf pandoc tex4ht texlive-full build-
essential emacs25-nox nano latexml bibtex2html fonts-freefont-otf fonts-
freefont-ttf ttf-mscorefonts-installer html2ps imagemagick auctex emacs-
goodies-el vim vim-latexsuite bibtexconv curl git  
# writer2latex  
## install latex2wp for wordpress export  
RUN curl -sSL https://get.haskellstack.org/ | sh  
RUN git clone https://github.com/cangiuli/latex2wp.git /tmp/latex2wp  
RUN cd /tmp/latex2wp && stack build --copy-bins --local-bin-
path=/usr/local/bin/  
RUN mv /usr/local/bin/latex2wp-exe /usr/local/bin/latex2wp  
RUN rm -rf /tmp/latex2wp  
  
ENV DISPLAY :0  

