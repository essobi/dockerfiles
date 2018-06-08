FROM skranz/rskranz:latest  
  
MAINTAINER Sebastian Kranz "sebastian.kranz@uni-ulm.de"  
# copy and run package installation file  
COPY install_rtutor.r /tmp/install1.r  
RUN Rscript /tmp/install1.r  
  
# Install large example problem sets  
COPY install_procurement.r /tmp/install2.r  
RUN Rscript /tmp/install2.r  
  
# Copy example problem sets from  
# from RTutorDocker repository  
COPY ps/Intro/* /home/rtutor/ps/Intro/  
COPY ps/Example/* /home/rtutor/ps/Example/  

