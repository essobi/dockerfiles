FROM rocker/rstudio  
FROM rocker/tidyverse  
COPY . /usr/local/src/scripts  
COPY ./scripts/* /usr/local/src/scripts  
WORKDIR /usr/local/src/scripts  
RUN apt-get update; \  
apt-get -y upgrade  
RUN apt-get -y install cmake libssl-dev  
RUN apt-get install -qqy x11-apps  
RUN apt-get install -y vim nano zsh curl git sudo  
RUN apt-get install -y x11vnc xvfb sudo  
RUN mkdir ~/.vnc  
RUN wget
https://github.com/stnava/ITKR/releases/download/latest/ITKR_0.4.12_R_x86_64-pc-
linux-gnu.tar.gz  
RUN wget
https://github.com/stnava/ANTsRCore/releases/download/v0.4.2.1/ANTsRCore_0.4.2.1_R_x86_64-pc-
linux-gnu.tar.gz  
RUN wget
https://github.com/stnava/ANTsR/releases/download/latest/ANTsR_0.6.1_R_x86_64-pc-
linux-gnu.tar.gz  
# https://github.com/stnava/ANTsR/releases/download/test/ANTsR_0.6.1.tar.gz  
RUN Rscript myantsr.R  
RUN R CMD INSTALL ITKR_0.4.12_R_x86_64-pc-linux-gnu.tar.gz  
RUN R CMD INSTALL ANTsRCore_0.4.2.1_R_x86_64-pc-linux-gnu.tar.gz  
RUN R CMD INSTALL ANTsR_0.6.1_R_x86_64-pc-linux-gnu.tar.gz  
CMD ["/init"]  

