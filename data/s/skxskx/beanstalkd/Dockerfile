#  
# Build it:  
# sudo docker build -t skxskx/beanstalkd .  
#  
# Then launch it:  
# sudo docker run -d -p 11300:11300 skxskx/beanstalkd  
#  
FROM ubuntu  
MAINTAINER steve@steve.org.uk  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -q update  
RUN apt-get -y install build-essential  
ADD http://github.com/kr/beanstalkd/archive/v1.9.tar.gz /tmp/  
RUN cd /tmp/v1.9.tar.gz/beanstalkd-1.9/ && make  
RUN cp /tmp/v1.9.tar.gz/beanstalkd-1.9/beanstalkd /usr/local/bin/  
EXPOSE 11300  
CMD ["/usr/local/bin/beanstalkd","-n"]  

