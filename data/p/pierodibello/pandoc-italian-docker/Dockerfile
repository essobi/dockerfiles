FROM jagregory/pandoc:latest  
  
MAINTAINER Pietro Di Bello <pierodibello@gmail.com>  
  
# install italian language  
RUN apt-get update -y \  
&& apt-get install -y -o Acquire::Retries=10 --no-install-recommends \  
texlive-lang-italian  

