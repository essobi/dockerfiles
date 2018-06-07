FROM rocker/r-ver:3.4.3  
LABEL maintainer="zamorarr"  
RUN apt-get -y update && apt-get install -y \  
git-core \  
libapparmor-dev \  
zlib1g-dev \  
libcurl4-openssl-dev \  
libssl-dev  
#RUN ["install2.r", "devtools"]  
#RUN ["R", "-e", "devtools::install_github('zamorarr/msf')"]  
RUN ["install2.r", "remotes"]  
RUN ["installGithub.r", "zamorarr/msf"]  
CMD ["R"]  
  

