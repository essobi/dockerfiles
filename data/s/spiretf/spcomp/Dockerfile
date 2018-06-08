from i386/ubuntu  
maintainer Robin Appelman <robin@icewind.nl>  
  
ADD ./install.sh /install.sh  
RUN mkdir /data \  
&& mkdir /include \  
&& apt-get update \  
&& apt-get install -y wget unzip \  
&& rm -rf /var/lib/apt/lists/*  
RUN /install.sh  
  
ADD ./spcomp.sh /spcomp.sh  
  
WORKDIR /data  
ENTRYPOINT ["/spcomp.sh"]  

