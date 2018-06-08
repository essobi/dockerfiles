FROM skranz/rskranz:latest  
  
MAINTAINER Sebastian Kranz "sebastian.kranz@uni-ulm.de"  
# copy and run package installation file  
COPY install.r /tmp/install.r  
RUN Rscript /tmp/install.r  
  
# copy and run package installation file  
COPY install2.r /tmp/install2.r  
RUN Rscript /tmp/install2.r  

