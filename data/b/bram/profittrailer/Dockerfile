FROM ubuntu:16.04  
  
MAINTAINER Beam <b-docker-profittrailer@grmbl.net>  
  
RUN apt-get update && apt-get upgrade -y --no-install-recommends  
RUN apt-get install -y --no-install-recommends curl unzip default-jdk  
  
  
#ENV PT_DOWNLOAD_URL=https://github.com/taniman/profit-
trailer/releases/download/v1.2.6.25/ProfitTrailer.zip  
ENV PT_DOWNLOAD_URL="https://github.com/taniman/profit-
trailer/releases/download/2.0.4/ProfitTrailer-2.0.4.zip"  
RUN cd /opt && curl -L -o ProfitTrailer.zip $PT_DOWNLOAD_URL && unzip
ProfitTrailer.zip && /bin/ln -s /opt/ProfitTrailer-* /opt/ProfitTrailer
2>/dev/null  
ADD run.sh /run.sh  
  
CMD /run.sh  
  
EXPOSE 8081  

