FROM debian:latest  
  
MAINTAINER Pavel Vondruska <vondruska@cesnet.cz>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends fakeroot \  
&& rm -r /var/lib/apt/lists/* \  
&& apt-get clean  
  
CMD ["bash"]  

