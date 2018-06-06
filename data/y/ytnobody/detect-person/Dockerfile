FROM ytnobody/base:wheezy  
MAINTAINER ytnobody <ytnobody@gmail.com>  
  
WORKDIR /root  
ADD app app  
  
WORKDIR /root/app  
RUN cpanm --installdeps --notest .  
  
EXPOSE 5500  
ENTRYPOINT ["morbo", "-l", "http://*:5500", "api.psgi"]

