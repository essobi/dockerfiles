FROM debian:stretch-slim  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qq \  
&& apt-get dist-upgrade -y -qq \  
&& apt-get install -y --no-install-recommends \  
texlive \  
texlive-base \  
texlive-font-utils \  
texlive-fonts-extra \  
texlive-fonts-recommended \  
texlive-lang-english \  
texlive-latex-base \  
texlive-latex-extra \  
texlive-latex-recommended \  
texlive-luatex \  
texlive-xetex \  
&& apt-get purge -y -qq ^tex.*-doc$ \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*  
  
WORKDIR /docs  
  
ENTRYPOINT ["xelatex"]  
  
CMD ["--help"]  

