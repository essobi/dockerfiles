# An interactive base image that runs commands as users rather than root  
FROM ubuntu:16.04  
MAINTAINER benjamin.gemmill@gmail.com  
  
RUN apt-get update && apt-get install -y locales && locale-gen en_US.UTF-8  
ENV LANG='en_US.UTF-8' LC_ALL='en_US.UTF-8'  
# universe and multiverse  
RUN sed -i 's/^#\s*\\(deb.*universe\\)$/\1/g' /etc/apt/sources.list  
RUN sed -i 's/^#\s*\\(deb.*multiverse\\)$/\1/g' /etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y \  
gosu  
  
COPY startup /etc/init/startup  
  
RUN apt-get purge -yq software-properties-common \  
&& apt-get autoremove -yq \  
&& apt-get autoclean -yq \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/etc/init/startup"]  

