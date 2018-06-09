FROM swiftdevel/swift  
  
RUN apt-get update \  
&& apt-get install -y curl apt-transport-https  
  
RUN curl http://download.tarantool.org/tarantool/1.7/gpgkey | apt-key add - \  
&& echo "deb http://download.tarantool.org/tarantool/1.7/ubuntu/ xenial main"
>> /etc/apt/sources.list.d/tarantool_1_7.list \  
&& echo "deb-src http://download.tarantool.org/tarantool/1.7/ubuntu/ xenial
main" >> /etc/apt/sources.list.d/tarantool_1_7.list  
  
RUN apt-get update \  
&& apt-get install -y tarantool tarantool-dev \  
&& rm -rf /var/lib/apt/lists/*  

