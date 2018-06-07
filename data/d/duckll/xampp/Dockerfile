FROM duckll/base  
  
MAINTAINER DuckLL <a347liao@gmail.com>  
  
EXPOSE 80  
# apt-get  
RUN apt-fast -y install \  
net-tools \  
&& apt-fast clean  
  
# install xampp  
RUN wget
http://nchc.dl.sourceforge.net/project/xampp/XAMPP%20Linux/7.0.9/xampp-
linux-x64-7.0.9-2-installer.run \  
&& chmod +x ./xampp-linux-x64-7.0.9-2-installer.run \  
&& ./xampp-linux-x64-7.0.9-2-installer.run \  
&& rm ./xampp-linux-x64-7.0.9-2-installer.run  
  
# set lnmp start  
RUN wget https://raw.githubusercontent.com/DuckLL/xampp/master/xampp.sh -O
/etc/my_init.d/xampp.sh \  
&& chmod +x /etc/my_init.d/xampp.sh  

