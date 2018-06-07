FROM fedora:latest  
MAINTAINER heichblatt  
  
RUN /bin/dnf install -y texlive \  
texlive-amsfonts \  
texlive-babel-german \  
texlive-latex \  
texlive-base \  
texlive-metafont-bin \  
texlive-texconfig \  
texlive-preprint \  
texlive-dinbrief \  
texlive-wrapfig \  
latexmk && \  
/bin/dnf clean all  
RUN /bin/mkdir -pv /target  
WORKDIR /target  
ADD ./entrypoint.sh /usr/bin/local/entrypoint.sh  
ENTRYPOINT ["/usr/bin/local/entrypoint.sh"]  

