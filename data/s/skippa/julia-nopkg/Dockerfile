# Julia language  
FROM skippa/base  
MAINTAINER mike.aizatsky@gmail.com  
  
RUN echo "deb http://ppa.launchpad.net/staticfloat/julia-deps/ubuntu xenial
main" > /etc/apt/sources.list.d/staticfloat-ubuntu-julia-deps-xenial.list  
RUN echo "deb http://ppa.launchpad.net/staticfloat/juliareleases/ubuntu xenial
main" > /etc/apt/sources.list.d/staticfloat-ubuntu-juliareleases-xenial.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys CF979FFA3D3D3ACC  
RUN apt-get update && apt-get install julia libzmq3-dev wget -y  
  
RUN julia -e "Pkg.init()"  
  
ENTRYPOINT ["julia"]  

