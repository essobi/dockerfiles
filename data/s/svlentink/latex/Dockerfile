# GPLv3  
FROM svlentink/texlive-with-libraries  
MAINTAINER svlentink  
LABEL Description="LaTeX docker with special powers"  
  
COPY latexBuilder.sh /usr/bin/latexBuilder  
COPY sh /usr/lib/latexBuilderScripts  
  
# http://docs.docker.com/engine/reference/builder/#entrypoint  
ENTRYPOINT ["/usr/bin/latexBuilder"]  
  
# runs during starting the container  
CMD ["--help"]  

