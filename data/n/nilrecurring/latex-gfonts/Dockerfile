FROM blang/latex  
  
WORKDIR /root  
  
## Latex package manager setup  
RUN apt-get update && apt-get install wget xzdec  
# Switching to old mirror because debian  
# Relevant SE answer: https://tex.stackexchange.com/questions/313768/why-
getting-this-error-tlmgr-unknown-directive  
RUN tlmgr init-usertree; tlmgr option repository
ftp://tug.org/historic/systems/texlive/2015/tlnet-final  
  
## Install latex-fontawesome  
RUN tlmgr install fontawesome  
  
## Install GFonts  
RUN apt-get install curl  
RUN wget https://raw.githubusercontent.com/qrpike/Web-Font-
Load/master/install_debian.sh  
RUN sed -i install_debian.sh -e "s/sudo //" -e "s/clear/set -e/" -e "s/rm /rm
-f /"  
RUN bash install_debian.sh  
  
## Update latex font cache with new fonts  
RUN luaotfload-tool -v -u  
  
WORKDIR /data  

