FROM fitra/ubuntu-minimalistic  
  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0x5a16e7281be7a449  
RUN echo "deb http://dl.hhvm.com/ubuntu trusty main" >>
/etc/apt/sources.list.d/hhvm.list \  
&& apt-get update -y \  
&& apt-get install -y sudo hhvm=3.13.1~trusty \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 9000  
CMD ["/usr/bin/hhvm", "-m", "server", "-c", "/etc/hhvm/server.ini"]  

