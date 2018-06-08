FROM phusion/baseimage:0.9.16  
MAINTAINER James White <dev.jameswhite+minicron@gmail.com>  
  
ENV TZ=Asia/Bangkok  
  
# Set the timezone.  
RUN echo $TZ > /etc/timezone  
RUN dpkg-reconfigure -f noninteractive tzdata  
  
# Install minicron install dependencies  
RUN apt-get update && apt-get install -y curl unzip  
  
RUN rm -f /etc/service/sshd/down  
  
# Install minicron  
ADD install.sh /  
RUN chmod +x /install.sh  
RUN /install.sh  

