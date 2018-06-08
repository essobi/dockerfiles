FROM ubuntu:16.04  
MAINTAINER Kazumichi Yamamoto <yamamoto.febc@gmail.com>  
LABEL MAINTAINER 'Kazumichi Yamamoto <yamamoto.febc@gmail.com>'  
  
RUN apt-get update && apt-get -y install \  
bash \  
git \  
make \  
zip \  
mkdocs \  
&& apt-get clean \  
&& rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
WORKDIR /workdir  
ENTRYPOINT ["mkdocs"]  
CMD ["build"]  

