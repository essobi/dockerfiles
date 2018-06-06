FROM joey711/dada2-base-devel  
  
LABEL project="dada2"  
LABEL application="RStudioIDE"  
  
MAINTAINER Paul McMurdie "paul.mcmurdie@wholebiome.com"  
RUN R -e "packageVersion('dada2')"  
  
EXPOSE 8787  
## automatically link a shared volume for kitematic users  
VOLUME /home/rstudio/kitematic  
  
CMD ["/init"]  

