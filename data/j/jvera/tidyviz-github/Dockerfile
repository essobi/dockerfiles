FROM jvera/base-extras:latest  
  
LABEL maintainer "vera.josemanuel@gmail.com"  
  
ADD github_installs.R /tmp/github_installs.R  
  
RUN Rscript /tmp/github_installs.R \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds  

