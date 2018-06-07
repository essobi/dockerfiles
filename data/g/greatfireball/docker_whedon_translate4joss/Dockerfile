FROM ubuntu  
  
RUN apt update && apt install pandoc git pandoc-citeproc texlive texlive-
latex-extra texlive-bibtex-extra biber texlive-fonts-recommended lmodern
texlive-xetex wget --yes --no-install-recommends && wget -O /tmp/pandoc.deb
https://github.com/jgm/pandoc/releases/download/2.1.1/pandoc-2.1.1-1-amd64.deb
&& dpkg -i /tmp/pandoc.deb && git clone
https://github.com/openjournals/whedon.git /tmp/whedon  
  
VOLUME /data  
WORKDIR /data  
  
ENTRYPOINT pandoc -o paper.pdf -V geometry:margin=1in --filter pandoc-citeproc
paper.md --template /tmp/whedon/resources/latex.template --variable
formatted_doi=pending -V joss_logo_path=/tmp/whedon/resources/joss-logo.png
--pdf-engine=xelatex  
  
CMD "--variable=repository:https://link-to-repo
--variable=archive_doi:https://archive-doi"  

