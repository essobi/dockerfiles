FROM rlum/core  
  
MAINTAINER "Christoph Burow" christoph.burow@gmx.net  
  
RUN . /etc/environment \  
&& install2.r --error \  
\--repos 'http://www.bioconductor.org/packages/release/bioc' \  
\--repos "https://mran.microsoft.com/" \  
\--deps "TRUE" \  
Luminescence RLumModel RLumShiny

