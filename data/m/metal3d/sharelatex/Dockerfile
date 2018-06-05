FROM sharelatex/sharelatex  
  
RUN sed -i 's/pdflatex -synctex=1/pdflatex -synctex=1 -shell-escape/'
/var/www/sharelatex/clsi/app/js/LatexRunner.js  
  
RUN set -xe; \  
wget -q https://examples.metal3d.org/texlive.tgz; \  
sleep 1; \  
tar zxf texlive.tgz; \  
rm -f texlive.tgz; \  
tlmgr install scheme-full --no-persistent-downloads --repository
$(pwd)/texlive || : ; \  
rm -rf texlive;  

