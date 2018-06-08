FROM mysql:5.7  
MAINTAINER Andrea Cattaneo <andrea.cattaneo.dev@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
#RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*  
## install tuning-primer  
#RUN curl -sL -o /usr/local/bin/tuning-primer 'https://launchpad.net/mysql-
tuning-primer/trunk/1.6-r1/+download/tuning-primer.sh' && \  
# chmod +x /usr/local/bin/tuning-primer  
RUN apt-get update && apt-get install -y net-tools bc socat && rm -rf
/var/lib/apt/lists/*  
  
ADD tuning-primer_auto.sh /usr/local/bin/tuning-primer_auto  
RUN chmod +x /usr/local/bin/tuning-primer_auto  
  
VOLUME ["/data"]  
  
WORKDIR /data  
  
ENTRYPOINT ["/usr/local/bin/tuning-primer_auto"]  
  
ADD https://launchpad.net/mysql-tuning-primer/trunk/1.6-r1/+download/tuning-
primer.sh /usr/local/bin/tuning-primer  
RUN chmod +x /usr/local/bin/tuning-primer  

