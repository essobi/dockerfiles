FROM ubuntu:14.04  
MAINTAINER ricardoamaro <ricardo.amaro@acquia.com>  
  
#COPY sources.list /etc/apt/sources.list  
ENV HOME /root  
#ADD . /build  
ENV DEBIAN_FRONTEND noninteractive  
# Keep upstart from complaining  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Install services  
RUN apt-get update  
RUN apt-get install -y --force-yes ssh cron wget curl python  
  
RUN useradd -ms /bin/bash paulstaab  
RUN mkdir -p /home/paulstaab/.ssh  
ADD authorized_keys_paulstaab /home/paulstaab/.ssh/authorized_keys  
RUN chmod 600 /home/paulstaab/.ssh/*  
RUN chown -R paulstaab:paulstaab /home/paulstaab  
  
ADD authorized_keys /authorized_keys  
ADD ./scripts/SSHdConfig.sh /SSHdConfig.sh  
RUN chmod 777 /SSHdConfig.sh  
RUN bin/bash /SSHdConfig.sh && rm /SSHdConfig.sh  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH fix for permanent login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
#ADD crontab /etc/crontab  
ADD crontab /var/spool/cron/crontabs/root  
RUN chmod 600 /var/spool/cron/crontabs/root  
  
# Scripts  
ADD ./scripts/start.sh /sbin/start.sh  
ADD ./scripts/sshd.sh /sbin/sshd.sh  
ADD ./scripts/cron.sh /sbin/cron.sh  
ADD ./scripts/YahuWorker.py /root/YahuWorker.py  
ADD ./scripts/YahuJsonTime.json /root/YahuJsonTime.json  
RUN touch /root/YahuWorker.log  
#RUN chmod 755 /root/YahuWorker.py  
RUN chmod 755 /root/YahuWorker.log  
  
# Make them executable  
RUN chmod 777 /sbin/start.sh /sbin/cron.sh /sbin/sshd.sh /root/YahuWorker.py  
  
EXPOSE 22  
CMD ["/bin/bash", "/sbin/start.sh"]  

