FROM rocker/r-ver:3.2.5  
  
RUN apt-get update -qq && apt-get -y --no-install-recommends install \  
libxml2-dev \  
libssl-dev \  
libcurl4-openssl-dev \  
wget \  
subversion \  
&& wget -q
https://github.com/jgm/pandoc/releases/download/1.19.2.1/pandoc-1.19.2.1-1-amd64.deb
\  
&& dpkg -i pandoc-1.19.2.1-1-amd64.deb \  
&& rm pandoc-1.19.2.1-1-amd64.deb \  
&& R -e "source(\"https://install-github.me/r-lib/remotes\")"  
  
COPY build.sh /home/docker/  
  
#WORKDIR /home/docker  
  
#ENTRYPOINT ["/home/docker/build.sh"]  

