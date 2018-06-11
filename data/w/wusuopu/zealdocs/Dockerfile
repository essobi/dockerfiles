FROM ubuntu:14.04  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& add-apt-repository -y ppa:zeal-developers/ppa \  
&& apt-get update \  
&& apt-get install -y zeal  
  
CMD ["zeal"]  

