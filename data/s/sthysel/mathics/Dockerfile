FROM python:3.5  
MAINTAINER https://github.com/sthysel/docker-mathics  
  
ENV VERSION 0.9  
RUN groupadd -g 1000 mathman  
RUN useradd --uid 1000 --gid 1000 mathman  
  
# install  
RUN mkdir /src/  
WORKDIR /src/  
  
RUN curl -sL https://github.com/mathics/Mathics/archive/v${VERSION}.tar.gz |
tar xz  
RUN cd ./Mathics-${VERSION} && python setup.py install  
  
VOLUME /work  
WORKDIR /work  
  
USER mathman  
  

