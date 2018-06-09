FROM ubuntu:latest  
MAINTAINER Yannic Schröder <schroeder@ibr.cs.tu-bs.de>  
RUN apt-get update -qy  
RUN apt-get install -y wget texlive-base texlive-latex-extra texlive-fonts-
extra latex-beamer texlive-fonts-recommended texlive-lang-german texlive-
extra-utils cm-super  
RUN wget http://tubslatex.ejoerns.de/1.1.0/tubslatex_installer  
RUN echo "d7340d663095024dafb5c9197aa0fcec138353cf2b1d10f589213b091d214f3c
*tubslatex_installer" | sha256sum -c -  
RUN wget http://tubslatex.ejoerns.de/1.1.0/tubslatex_1.1.0.tds.zip  
RUN echo "cf026f69eba8fb6c2484a25962e385ace16bce328fe9e49ccaaa7bfd757668d5
*tubslatex_1.1.0.tds.zip" | sha256sum -c -  
RUN yes | sh tubslatex_installer tubslatex_1.1.0.tds.zip

