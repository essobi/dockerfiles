FROM rocker/rstudio:3.4.2  
# Update the system and install software:  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y nano vim curl keychain openssl libsasl2-dev libmariadb-
client-lgpl-dev liblzma-dev libbz2-dev libpcre3-dev build-essential libicu-dev
default-jdk default-jre  
  
# Added GIT LFS support:  
RUN \  
curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | bash && \  
apt-get install git-lfs && \  
git lfs install  
  
# Add archived CRAN packages:  
RUN \  
cd /home && \  
wget http://cran.wustl.edu/src/contrib/Archive/Rstem/Rstem_0.4-1.tar.gz && \  
wget
https://cran.r-project.org/src/contrib/Archive/sentiment/sentiment_0.2.tar.gz  
  
# Define known ENV variables:  
ENV \  
PASSWORD=xdRNgr@UAFTFkI6 \  
USER=RStudio  
  
CMD ["/init"]  

