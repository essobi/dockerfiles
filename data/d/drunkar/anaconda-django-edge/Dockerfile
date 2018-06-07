FROM ubuntu:16.04  
MAINTAINER drunkar <drunkars.p@gmail.com>  
  
# locale for tokyo  
RUN apt-get update && \  
apt-get -y install tzdata locales && \  
ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
# Install wget and build-essential  
RUN apt-get update && apt-get install -y \  
build-essential \  
wget  
  
##############################################################################  
# anaconda python  
##############################################################################  
# Install Anaconda  
RUN apt-get update && \  
apt-get install -y wget bzip2 ca-certificates  
  
RUN wget --quiet
https://repo.continuum.io/archive/Anaconda3-4.4.0-Linux-x86_64.sh && \  
/bin/bash Anaconda3-4.4.0-Linux-x86_64.sh -b -p /opt/conda && \  
rm Anaconda3-4.4.0-Linux-x86_64.sh  
  
ENV PATH /opt/conda/bin:$PATH  
RUN pip install --upgrade pip  
  
  
##############################################################################  
# Django  
##############################################################################  
ENV DJANGO_VERSION 1.11.4  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
postgresql-client \  
&& rm -rf /var/lib/apt/lists/*  
RUN pip install psycopg2 django=="$DJANGO_VERSION"  
  
ADD entrypoint.sh /root/entrypoint.sh  
EXPOSE 8000  
WORKDIR /usr/src/app  
VOLUME ["/usr/src/app"]  
CMD ["/root/entrypoint.sh"]  

