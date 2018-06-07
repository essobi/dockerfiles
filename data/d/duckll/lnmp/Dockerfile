FROM duckll/base  
  
MAINTAINER DuckLL <a347liao@gmail.com>  
  
EXPOSE 80  
  
# apt-get  
RUN apt-fast update \  
&& apt-fast -y install \  
net-tools \  
&& apt-fast clean \  
  
# install lnmp  
&& wget http://soft.vpser.net/lnmp/lnmp1.3.tar.gz && tar -xvf ./lnmp1.3.tar.gz
\  
&& cd lnmp1.3 && wget
https://raw.githubusercontent.com/DuckLL/lnmp/master/install.conf && cat
install.conf | ./install.sh \  
&& cd ../ && rm -rf lnmp1.3.tar.gz lnmp1.3 \  
  
# set lnmp start  
&& wget https://raw.githubusercontent.com/DuckLL/lnmp/master/lnmp.sh -O
/etc/my_init.d/lnmp.sh \  
&& chmod +x /etc/my_init.d/lnmp.sh  

