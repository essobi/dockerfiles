FROM pboreg/latex  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get -yq install --no-install-recommends \  
wget xzdec unzip && \  
tlmgr update --self --all && \  
tlmgr install \  
animate \  
beamer \  
datetime \  
fmtcount \  
media9 \  
ocgx2 \  
pgf \  
xpatch && \  
apt-get purge -yq \  
wget xzdec unzip && \  
apt-get autoremove -yq && \  
apt-get clean -yq && \  
rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/root/texmf/web2c/tlmgr.log  
  
# Install DTU beamer templates from GitLab repo (master branch)  
RUN apt-get update && \  
apt-get -yq install --no-install-recommends \  
wget ca-certificates && \  
cd ~/texmf && \  
wget -nv -O- \  
https://gitlab.gbar.dtu.dk/latex/dtutemplates/repository/archive.tar?ref=master
| \  
tar x --strip 1 && \  
texhash --verbose && \  
apt-get purge -yq \  
wget ca-certificates && \  
apt-get autoremove -yq && \  
apt-get clean -yq && \  
rm -rf /var/lib/apt/lists/* \  
/tmp/*  

