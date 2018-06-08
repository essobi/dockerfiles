FROM trestletech/plumber:travis  
  
RUN R --no-restore \--no-save -e \  
'repo <\- "http://cran.us.r-project.org";install.packages("tidyverse",
repos=repo);install.packages("car", repos=repo)'  

