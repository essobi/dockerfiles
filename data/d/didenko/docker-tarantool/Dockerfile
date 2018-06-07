FROM ubuntu:latest  
  
MAINTAINER Aleksandr Didenko <aa.didenko@yandex.com>  
  
RUN apt-get update  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y curl lsb-release  
  
RUN curl -s http://tarantool.org/dist/public.key | apt-key add --  
RUN touch /etc/apt/sources.list.d/tarantool.list  
RUN echo "deb http://tarantool.org/dist/ubuntu/ $(lsb_release -cs) main" >>
/etc/apt/sources.list.d/tarantool.list  
RUN echo "deb-src http://tarantool.org/dist/ubuntu/ $(lsb_release -cs) main"
>> /etc/apt/sources.list.d/tarantool$  
RUN apt-get update  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y tarantool tarantool-
client  
  
ADD tarantool.cfg /etc/tarantool/tarantool.cfg  
  
EXPOSE 33013 33014 33015  
RUN tarantool_box --init-storage  
  
ENTRYPOINT ["/usr/bin/tarantool_box"]

