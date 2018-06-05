FROM nvidia/caffe:0.14  
MAINTAINER Weitao Zhou <wtzhou@dataman-inc.com>  
  
RUN rm -rf /var/lib/apt/lists/* && apt-get update && apt-get install -y
openssh-server  
RUN mkdir /var/run/sshd  
  
RUN echo 'root:password' | chpasswd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN env |grep -iE "caffe|cuda|nvidia|cudnn" | sed 's/^/export &/g' >
/etc/profile.d/caffe-env.sh  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

