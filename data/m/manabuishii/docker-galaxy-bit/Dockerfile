FROM ubuntu:14.04.4  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq ; apt-get upgrade ; \  
apt-get install -y curl git make locales python gridengine-drmaa1.0 pbs-drmaa1
slurm-drmaa1 gridengine-client; \  
apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
  
# Locale  
RUN locale-gen en_US.UTF-8 ; update-locale LANG=en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
# Galaxy user account  
RUN useradd -m galaxy  
RUN echo "galaxy:galaxy" | chpasswd  
RUN echo "galaxy ALL = NOPASSWD : ALL" >> /etc/sudoers  
USER galaxy  
WORKDIR /home/galaxy  
# Galaxy source  
RUN curl --silent -L
https://github.com/galaxyproject/galaxy/archive/v15.07.tar.gz | tar zxf -  
RUN chown -R galaxy.galaxy ./galaxy-15.07  
RUN sed 's/^#host = 127.0.0.1/host = 0.0.0.0/'
/home/galaxy/galaxy-15.07/config/galaxy.ini.sample >
/home/galaxy/galaxy-15.07/config/galaxy.ini  
RUN cd /home/galaxy/galaxy-15.07 ; ./scripts/common_startup.sh  
RUN cd /home/galaxy/galaxy-15.07 ; ./create_db.sh  
USER root  
ADD start.sh /usr/local/bin/start.sh  
  
CMD ["/usr/local/bin/start.sh"]  

