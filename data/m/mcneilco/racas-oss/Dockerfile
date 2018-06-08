FROM mcneilco/centos-r-repo:mailr  
  
COPY . /home/runner/racas  
  
USER runner  
RUN export R_LIBS=/home/runner/build/r_libs && R CMD INSTALL --no-multiarch
--with-keep.source /home/runner/racas  
  
USER root  
RUN rm -rf /home/runner/racas  
EXPOSE 1080  

