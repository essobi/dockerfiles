  
FROM ubuntu:latest  
  
LABEL maintainer="Matthias Lohr <mail@mlohr.com>"  
RUN apt-get update \  
&& apt-get install -y make texlive-latex-base texlive-latex-recommended
texlive-latex-extra \  
texlive-fonts-recommended texlive-fonts-extra \  
texlive-lang-german \  
&& apt-get clean \  
&& for i in $(find /var/lib/apt/lists/ -type f) ; do rm $i ; done  
  

