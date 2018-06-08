# install ruby from Official Ubuntu base image  
FROM sawanoboly/rbenv1404  
MAINTAINER SAWANOBORI Yukihiko <sawanoboriyu@higanworks.com>  
  
WORKDIR /root  
RUN apt-get -qqy install ruby  
## 1.9.2-p326 will fail to building on ubuntu 14.04  
RUN /root/.rbenv/bin/rbenv install 1.9.2-p320  
RUN apt-get -qqy remove ruby  
ENV PATH ~/.rbenv/versions/1.9.2-p320/bin:$PATH  
RUN /root/.rbenv/versions/1.9.2-p320/bin/gem update --system --no-ri --no-rdoc
-q  
RUN /root/.rbenv/versions/1.9.2-p320/bin/gem install bundler --no-ri --no-rdoc
-q  

