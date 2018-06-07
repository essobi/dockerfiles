FROM jenkinsci/slave  
  
USER root  
RUN apt-get update \  
&& apt-get install -q -y \  
git build-essential subversion libncurses5-dev zlib1g-dev unzip ccache \  
gawk wget libssl-dev libxml-parser-perl file rsync groff-base  
  
USER jenkins  

