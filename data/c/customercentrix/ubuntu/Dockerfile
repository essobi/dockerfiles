FROM ubuntu:14.04.1  
# Ubuntu 14.04.1 LTS  
  
RUN date -u +"%Y-%m-%d %H:%M:%S" && sed -i 's/# \\(.*multiverse$\\)/\1/g'
/etc/apt/sources.list \  
&& date -u +"%Y-%m-%d %H:%M:%S" && apt-get update \  
&& date -u +"%Y-%m-%d %H:%M:%S" && apt-get -y upgrade \  
&& date -u +"%Y-%m-%d %H:%M:%S" && apt-get install -y build-essential python \  
&& date -u +"%Y-%m-%d %H:%M:%S" && apt-get install -y software-properties-
common \  
&& date -u +"%Y-%m-%d %H:%M:%S" && apt-get install -y byobu curl git htop man
unzip vim wget pv \  
&& date -u +"%Y-%m-%d %H:%M:%S" && rm -rf /var/lib/apt/lists/* \  
&& date -u +"%Y-%m-%d %H:%M:%S"  

