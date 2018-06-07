# Run thunderbird with torbirdy and enigmail in a container  
  
FROM ubuntu:16.04  
MAINTAINER John Nagro <john.nagro@gmail.com>  
  
RUN apt-get clean && apt-get update  
RUN apt-get install -y \  
thunderbird \  
xul-ext-torbirdy \  
enigmail \  
unity-gtk-module-common \  
libcanberra-gtk-module \  
xauth \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT [ "thunderbird" ]  

