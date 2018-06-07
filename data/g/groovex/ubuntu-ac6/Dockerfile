FROM ubuntu:16.04  
MAINTAINER gx-dev@groove-x.com  
  
# apt  
RUN apt update  
RUN apt install -y cmake make gcc g++ gcc-arm-none-eabi git cppcheck default-
jre curl expect ruby ruby-dev gksu lib32ncurses5  
  
# copy install scripts  
COPY install_sw4stm32_linux_64bits-v2.3.run
/tmp/install_sw4stm32_linux_64bits-v2.3.run  
COPY install_ac6.sh /tmp/install_ac6.sh  
  
# copy workspace  
COPY workspace /root/workspace  
  
# setup package_cloud  
RUN gem install rake  
RUN gem install package_cloud --no-ri --no-rdoc  
  
# install ac6  
RUN /tmp/install_ac6.sh  
  

