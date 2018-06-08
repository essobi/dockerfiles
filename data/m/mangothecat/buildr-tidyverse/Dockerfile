FROM mangothecat/buildr:3.4.1  
RUN . /etc/environment \  
&& install2.r --error \  
\--repos 'http://www.bioconductor.org/packages/release/bioc' \  
\--repos $MRAN \  
tidyverse \  
testthat  

