FROM pboreg/latex  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get -yq install --no-install-recommends \  
wget xzdec unzip texlive-font-utils ghostscript && \  
tlmgr update --self --all && \  
tlmgr install \  
hyphenat \  
lastpage \  
multirow \  
pgf \  
siunitx \  
soul \  
tabto-ltx \  
titlesec && \  
apt-get purge -yq \  
wget xzdec unzip && \  
apt-get autoremove -yq && \  
apt-get clean -yq && \  
rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/root/texmf/web2c/tlmgr.log  
  

