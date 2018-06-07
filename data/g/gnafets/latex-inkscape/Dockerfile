FROM debian:testing  
  
RUN apt-get update && apt-get install -y \  
wget \  
git \  
make \  
texlive-full \  
inkscape && \  
# Removing documentation packages *after* installing them is kind of hacky,  
# but it only adds some overhead while building the image.  
apt-get \--purge remove -y .\\*-doc$ && \  
# Remove more unnecessary stuff  
apt-get clean -y && \  
# Add latexmkrc to always use shell-escape for inkscape  
echo "\$latex = 'latex %O --shell-escape %S';" | tee ~/.latexmkrc && \  
echo "\$pdflatex = 'pdflatex %O --shell-escape %S';" | tee -a ~/.latexmkrc  

