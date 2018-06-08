FROM ubuntu:trusty  
MAINTAINER njtobj <cnjsnjjn@163.com> (@njtobj)  
  
RUN apt-get update && apt-get install -y \  
libgtk2.0-dev \  
libgl1-mesa-dev \  
libmysqlclient-dev \  
\--no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
RUN /usr/share/locales/install-language-pack en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
ENV LANG=en_US.UTF-8  
VOLUME ["/hyd-scada"]  

