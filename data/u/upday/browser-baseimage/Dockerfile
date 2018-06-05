FROM phusion/baseimage:0.9.22  
#Dependencies  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
  
RUN apt-get update && \  
apt-get install -y openjdk-8-jdk \  
maven \  
build-essential \  
nodejs \  
libnss3 \  
libgconf-2-4  
  
RUN apt-get install -y chromium-browser \  
xvfb \  
libav-tools  
  
# Add Xvfb to runit  
RUN mkdir /etc/service/xvfb  
ADD scripts/run_xvfb.sh /etc/service/xvfb/run  
RUN chown root /etc/service/xvfb/run && \  
chmod 0755 /etc/service/xvfb/run  
ENV DISPLAY=:0  
# Set timezone  
ENV TZ Europe/Berlin  
RUN echo $TZ > /etc/timezone && \  
apt-get update && apt-get install -y tzdata && \  
rm /etc/localtime && \  
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \  
dpkg-reconfigure -f noninteractive tzdata && \  
apt-get clean  

