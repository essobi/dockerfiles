FROM openjdk:8  
  
RUN ln -sf /bin/bash /bin/sh # make bash the default shell (dash is used
before)  
  
# -zip: to package and compress artefacts (zip files are easier to open on
windows)  
RUN apt-get update && apt-get install -y \  
zip \  
&& rm -rf /var/lib/apt/lists/*  

