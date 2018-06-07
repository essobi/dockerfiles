FROM derekamz/awscli:latest  
  
ENV PATH="/opt/gcc-arm-none-eabi/bin:${PATH}"  
RUN apt-get update -y && apt-get install -y --no-install-recommends git bzip2
lib32z1 lib32ncurses5 \  
&& rm -rf /var/lib/apt/lists/*  
ADD https://launchpad.net/gcc-arm-embedded/5.0/5-2016-q3-update/+download/gcc-
arm-none-eabi-5_4-2016q3-20160926-linux.tar.bz2 /tmp/  
RUN tar -xjf /tmp/gcc-arm-none-eabi-5_4-2016q3-20160926-linux.tar.bz2 -C /tmp/
\  
&& mv /tmp/gcc-arm-none-eabi-5_4-2016q3 /opt/gcc-arm-none-eabi \  
&& rm -rf /tmp/*

