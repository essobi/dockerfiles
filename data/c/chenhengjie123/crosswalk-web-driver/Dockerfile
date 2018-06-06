# Set the base image to ubuntu  
FROM webratio/android-sdk  
# File Author / Maintainer  
MAINTAINER chenhengjie <chenhengjie123@gmail.com>  
  
# Install git  
RUN apt-get update  
RUN echo y | apt-get install git  
  
# Install lsusb  
RUN echo y | apt-get install usbutils  
  
# Install share libraries for xwalkdriver  
RUN echo y | apt-get install libglib2.0-0 libnss3 libxi6 libgconf-2-4  
  
# Install xwalkdriver  
ENV XWALKDRIVER_URL https://github.com/crosswalk-project/crosswalk-web-
driver.git  
  
RUN cd /opt && \  
git clone ${XWALKDRIVER_URL} && \  
ls  
  
# port expose  
EXPOSE 9515 5037 5554 5555  
# start adb server and check devices  
# start xwalkdriver server and accept all ips  
CMD adb devices && /opt/crosswalk-web-driver/bin/xwalkdriver64_release
--verbose --whitelisted-ips 0.0.0.0  

