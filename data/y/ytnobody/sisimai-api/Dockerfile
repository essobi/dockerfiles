FROM ytnobody/alpine-perl:latest  
MAINTAINER ytnobody <ytnobody@gmail.com>  
  
WORKDIR /root  
  
RUN cpm install Sisimai  
ADD app.psgi /root/app.psgi  
  
EXPOSE 5000  
CMD plackup -I local/lib/perl5 app.psgi  

