# Use an official R runtime as a parent image  
FROM r-base:3.4.4  
# Set the working directory  
WORKDIR /usr/local/project  
  
# Copy the current directory contents into the container at the working
directory  
COPY . /usr/local/project  
  
RUN apt-get update && apt-get install -y \  
libxml2-dev \  
libcurl4-openssl-dev \  
libssl-dev \  
&& Rscript -e "install.packages('packrat')" \  
&& Rscript install.R  
  
# Set the working directory  
WORKDIR /usr/local/project/csx415-project  
  
ENTRYPOINT exec /usr/bin/bash  

