From vacation/idp:0.1.10  
# IDP-fusion is Apache 2.0 but other softwares included such as GMAP have
other licenses  
# Please heed license requirements of all the softwares included in the docker  
#set up environment  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
libyaml-dev  
  
# Get STAR  
RUN cd /Source \  
&& curl -L https://github.com/alexdobin/STAR/archive/2.5.3a.tar.gz \  
| tar -xz \  
&& cp /Source/STAR-2.5.3a/bin/Linux_x86_64/* /usr/local/bin/ \  
&& rm -r /Source/STAR-2.5.3a  
  
# Get IDP-fusion  
RUN cd /Source \  
&& git clone https://github.com/jason-weirather/IDP-fusion.git  
# && cd IDP-fusion  
ENV PATH="/Source/IDP-fusion/bin:${PATH}"  

