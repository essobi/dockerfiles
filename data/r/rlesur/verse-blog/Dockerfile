FROM rocker/verse:3.4.3  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
whois \  
r-cran-rgl \  
mesa-common-dev \  
libglu1-mesa-dev \  
freeglut3-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/  
  
RUN Rscript -e "devtools::install_github('hadley/emo')"  
  
RUN install2.r --error --deps TRUE \  
blogdown \  
plot3D \  
rgl \  
plot3Drgl \  
animation \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds \  
&& Rscript -e "blogdown::install_hugo()"  
  
RUN mkdir /home/rstudio/bin \  
&& cp /root/bin/hugo /home/rstudio/bin/  

