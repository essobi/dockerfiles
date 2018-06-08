# meedan/fdupes  
# from ubuntu 12.04 which includes an fdupes which allows hardlinking with
`-L`  
FROM ubuntu:12.04  
MAINTAINER sysops@meedan.com  
  
# no recommended or suggested packages required  
RUN echo 'APT::Install-Recommends "0";' >> /etc/apt/apt.conf.d/01norecommend \  
&& echo 'APT::Install-Suggests "0";' >> /etc/apt/apt.conf.d/01norecommend  
  
RUN apt-get update --fix-missing \  
&& apt-get install -qy \  
fdupes  
  
CMD ["/usr/bin/fdupes"]  

