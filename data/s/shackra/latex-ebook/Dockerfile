FROM debian:jessie  
MAINTAINER Jorge Araya Navarro <elcorreo@deshackra.com>  
  
RUN apt-get update --fix-missing -qq -y \  
&& apt-get install -y \  
texlive-latex-base \  
texlive-xetex \  
texlive-extra-utils \  
texlive-lang-spanish \  
tidy \  
curl \  
zip \  
wget \  
uuid-runtime \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
  
ADD process.bash /root/  
RUN chmod +x /root/process.bash  
  
ENTRYPOINT /root/process.bash -  

