FROM ubuntu  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y cmatrix \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["cmatrix"]  
  

