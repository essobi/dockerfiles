# Protocol multiplexing in case some ports aren't available  
FROM ubuntu:latest  
MAINTAINER benjamin.gemmill@gmail.com  
  
RUN apt-get update && apt-get install -y locales && locale-gen en_US.UTF-8  
ENV LANG='en_US.UTF-8' LC_ALL='en_US.UTF-8'  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
sslh iproute2  
  
EXPOSE 443  
COPY startup /etc/init/startup  
  
RUN apt-get purge -yq software-properties-common \  
&& apt-get autoremove -yq \  
&& apt-get autoclean -yq \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["/etc/init/startup"]  

