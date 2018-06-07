FROM ubuntu:bionic  
  
VOLUME /usr/src/app  
WORKDIR /usr/src/app  
  
RUN apt-get -qq update && apt-get install -y --no-install-recommends
fontconfig fonts-lmodern texlive-latex-base texlive-latex-recommended texlive-
fonts-recommended texlive-luatex texlive-xetex texlive-latex-extra  
COPY fonts/ /usr/src/app/fonts  
RUN find fonts/ -name '*.ttf' -exec cp {} /usr/share/fonts/truetype \; && fc-
cache -f -v  
CMD xelatex -interaction=nonstopmode -halt-on-error -output-directory _build
neilgrogan-resume.tex  
  

