FROM rocker/tidyverse  
# Change environment to Japanese(Character and DateTime)  
ENV LANG ja_JP.UTF-8  
ENV LC_ALL ja_JP.UTF-8  
RUN sed -i '$d' /etc/locale.gen \  
&& echo "ja_JP.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen ja_JP.UTF-8 \  
&& /usr/sbin/update-locale LANG=ja_JP.UTF-8 LANGUAGE="ja_JP:ja"  
RUN /bin/bash -c "source /etc/default/locale"  
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
# Install packages  
RUN apt-get update -qq && apt-get -y --no-install-recommends install ed  
RUN Rscript -e
"install.packages(c('githubinstall','rstan','ggmcmc','rstanarm','ellipse','hexbin','ggtern','mvtnorm','bda','Nippon','ggrepel','data.table'))"  
  
CMD ["/init"]  

