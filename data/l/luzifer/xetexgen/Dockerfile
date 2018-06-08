FROM ubuntu  
  
MAINTAINER Knut Ahlers <knut@ahlers.me>  
  
ENV DEBIAN_FRONTEND=noninteractive  
ENV PACKAGES \  
texlive-xetex \  
texlive-latex-extra \  
texlive-latex-recommended \  
texlive-fonts-recommended \  
texlive-lang-european \  
texlive-lang-german  
  
RUN apt-get update \  
&& apt-get install -y $PACKAGES \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD ./generate-pdf /usr/local/bin/generate-pdf  
  
VOLUME ["/src"]  
WORKDIR /src  
  
ENTRYPOINT ["/usr/local/bin/generate-pdf"]  

