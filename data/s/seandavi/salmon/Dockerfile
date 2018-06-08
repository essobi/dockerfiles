############################################################  
# Dockerfile to build lofreq variant caller container  
# Based on Ubuntu  
#  
# lofreq is on the path  
#  
# usage:  
# docker run seandavi/lofreq lofreq ....  
#  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu  
  
# File Author / Maintainer  
MAINTAINER Sean Davis <seandavi@gmail.com>  
  
# Update the repository sources list  
RUN apt-get update --fix-missing  
RUN apt-get install -y wget python bzip2  
RUN apt-get install -y sysstat openjdk-8-jre-headless  
  
RUN echo 'ENABLED="true"' > /etc/default/sysstat  
RUN echo "PATH=/usr/lib/sysstat:/usr/sbin:/usr/sbin:/usr/bin:/sbin:/bin" >
/etc/cron.d/sysstat  
RUN echo "* * * * * root command -v debian-sa1 > /dev/null && debian-sa1 1
1\n" >> /etc/cron.d/sysstat  
  
  
COPY log_sar /tmp/log_sar  
RUN chmod +x /tmp/log_sar  
  
RUN mkdir -p /opt/  
WORKDIR /opt/  
  
# sambamba  
RUN wget
https://github.com/lomereiter/sambamba/releases/download/v0.6.5/sambamba_v0.6.5_linux.tar.bz2  
RUN tar -xvjf sambamba_v0.6.5_linux.tar.bz2  
RUN ln -s /opt/sambamba_v0.6.5 /usr/bin/sambamba  
  
# picard  
# Run as java -jar $PICARD  
RUN wget
https://github.com/broadinstitute/picard/releases/download/2.9.0/picard.jar  
ENV PICARD /opt/picard.jar  
  
  
#  
RUN wget https://github.com/COMBINE-
lab/salmon/releases/download/v0.8.1/Salmon-0.8.1_linux_x86_64.tar.gz  
RUN tar -xvzf Salmon-0.8.1_linux_x86_64.tar.gz  
  
  
  
RUN ln -s /opt/Salmon-0.8.1_linux_x86_64/bin/salmon /usr/bin/salmon  

