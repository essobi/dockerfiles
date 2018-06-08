FROM pomin5/ssh  
MAINTAINER Pomin Wu <pomin5@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
ENV REFRESHED_AT 2014-12-08  
RUN apt-get update && \  
apt-get install -yq vsftpd && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo "local_enable=YES" >> /etc/vsftpd.conf  
RUN echo "write_enable=YES" >> /etc/vsftpd.conf  
RUN echo "local_umask=022" >> /etc/vsftpd.conf  
RUN sed -i "s/anonymous_enable=YES/anonymous_enable=NO/" /etc/vsftpd.conf  
  
#RUN groupadd -g 1000 app && \  
# useradd -u 1000 -g app --home-dir /app -m app  
VOLUME ["/root", "/app"]  
  
#ADD init.sh /init.sh  
ADD run.sh /run.sh  
  
EXPOSE 21  
CMD ["/run.sh"]  

