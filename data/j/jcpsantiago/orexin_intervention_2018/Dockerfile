FROM rocker/tidyverse:3.4.4  
RUN install2.r --error \  
\--deps TRUE \  
stringi \  
zoo \  
lme4 \  
lmerTest \  
ggpubr \  
broman \  
emmeans \  
afex \  
&& R -e "devtools::install_github('hrbrmstr/hrbrthemes')"  
RUN apt-get install -y --no-install-recommends \  
fonts-roboto  

