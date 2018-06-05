FROM debian:stretch  
LABEL "MAINTAINER"="Sakarin Kammanee <Sakarin@coe.phuket.psu.ac.th>"  
  
ENV TZ=Asia/Bangkok  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN apt-get update && \  
apt-get -y install beanstalkd --no-install-recommends  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/var/lib/data"]  
EXPOSE 11300  
CMD ["/usr/bin/beanstalkd", "-l", "0.0.0.0", "-f", "60000", "-b",
"/var/lib/data", "-z", "5000000000"]  

