FROM debian:stable  
MAINTAINER Stepan Koci <stepan.koci@gmail.com>  
  
ENV HOME /root  
ENV TERM xterm  
ENV TAG 56  
COPY . /resources  
  
RUN sh /resources/shared/base/install.sh  
RUN sh /resources/shared/base/configure.sh  
  
RUN sh /resources/install.sh  
RUN sh /resources/configure.sh  
  
RUN sh /resources/shared/postgres94/install.sh  
RUN sh /resources/shared/postgres94/configure.sh  
  
RUN sh /resources/shared/node/install.sh  
  
EXPOSE 80  
EXPOSE 443  
WORKDIR /var/www/html  
  
CMD /resources/shared/base/container-cmd.sh

