# Sphinx v1.7 with Japanese  
#  
# docker run --rm -v `pwd`:/doc -w /doc pottava/sphinx:1.7jp /bin/sh -c "make
clean && make latex && cd _build/latex && uplatex -interaction=nonstopmode
sample.tex && dvipdfmx sample.dvi"  
  
FROM pottava/sphinx:1.7  
  
RUN apk --no-cache add --virtual build-deps fontconfig \  
&& tlmgr install \  
collection-latexrecommended collection-fontsrecommended \  
collection-latexextra collection-langjapanese \  
&& fc-cache -fv \  
&& apk del --purge -r build-deps  

