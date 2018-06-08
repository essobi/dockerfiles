FROM rocker/verse:3.4.1  
  
RUN apt-get update \  
&& apt-get install -y \  
pandoc \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/ \  
&& install2.r --error \--deps TRUE \  
argparse  

