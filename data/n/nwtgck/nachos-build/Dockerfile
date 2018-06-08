FROM i386/ubuntu:14.04  
  
LABEL maintainer="Ryo Ota <nwtgck@gmail.com>"  
# ==== Start Installation of requirements ====  
RUN apt update && apt install -y \  
ed \  
build-essential \  
g++-4.6 \  
&& rm -rf /var/lib/apt/lists/*  
# ==== End Installation of requirements ====  
# Done!  

