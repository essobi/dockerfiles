FROM centos:7  
MAINTAINER Sergey Ustyuzhanin SibData Company <dir@sibdata.ru>  
  
RUN localedef -i ru_RU -f UTF-8 ru_RU.UTF-8  
  
ENV LANG ru_RU.UTF-8  
COPY scripts/ /  
  
RUN /install.sh  
  
VOLUME "/root/billing"  
  
ENTRYPOINT ["/start.sh"]  
  
CMD ["/usr/local/billing/LBcore","-n","-c","/root/billing/conf/billing.conf"]  

