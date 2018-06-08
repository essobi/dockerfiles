FROM centos  
LABEL Maintainer="Babbage"  
  
# add mirror  
COPY ./tsinghua-mirrors-CentOS-Base.repo CentOS-Base.repo  
RUN mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak
&& \  
mv ./CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo  
  
RUN yum update; yum makecache;  
  
# set localtime and timezone  
ARG TZ=UTC  
ENV TZ ${TZ}  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# do some cleaning work  
RUN yum clean all && \  
rm -rf /var/cache/yum;  
  
#in the end  
VOLUME [ "/sys/fs/cgroup" ]  
CMD ["/usr/sbin/init"]  
  

