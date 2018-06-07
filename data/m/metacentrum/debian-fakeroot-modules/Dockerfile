FROM debian:latest  
  
MAINTAINER Pavel Vondruska <vondruska@cesnet.cz>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends fakeroot libx11-6 \  
&& rm -r /var/lib/apt/lists/* \  
&& apt-get clean  
  
RUN mkdir /afs /packages /auto /storage /scratch  
  
RUN ln -sf /afs/ics.muni.cz/software /software  
  
CMD ["bash"]  

