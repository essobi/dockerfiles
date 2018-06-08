FROM jpbernius/xelatex:latest  
  
MAINTAINER Jan Philip Bernius <janphilip@bernius.net>  
  
# install latex packages  
RUN apt-get update -y \  
&& apt-get install -y --no-install-recommends \  
pandoc \  
pandoc-citeproc  
  
WORKDIR /source  
  
ENTRYPOINT ["/usr/bin/pandoc"]  
  
CMD ["--help"]

