FROM debian  
MAINTAINER termoshtt <toshiki.teramura@gmail.com>  
RUN apt-get update && apt-get -y install \  
curl \  
latexdiff \  
latexmk \  
make \  
git \  
patch \  
texlive \  
texlive-lang-japanese \  
texlive-xetex \  
texlive-fonts-extra \  
texlive-latex-extra \  
texlive-luatex \  
texlive-publishers \  
texlive-math-extra \  
texlive-science \  
texlive-metapost \  
&& apt-get clean  
COPY .latexmkrc /root/  
WORKDIR /src  

