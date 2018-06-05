FROM dockerfile/java  
  
MAINTAINER Naoki AINOYA <ainonic@gmail.com>  
  
RUN apt-get -y install python-setuptools maven  
RUN easy_install pip  
  
# setup ssh server  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  
RUN sed -ri 's/PermitRootLogin without-password/PermitRootLogin yes/g'
/etc/ssh/sshd_config  
RUN echo 'root:redpen' | chpasswd  
  
# setup maven  
RUN apt-get -y install maven  
  
# setup supervisord  
RUN pip install supervisor  
RUN mkdir -p /etc/supervisord.d/  
RUN mkdir -p /var/log/supervisor  
ADD template/supervisord.conf /etc/supervisord.conf  
ADD template/supervisord.d/redpen.ini /etc/supervisord.d/redpen.ini  
  
# set redpen env  
ENV REDPEN_HOME /  
  
# setup redpen  
RUN mkdir -p /home/redpen  
WORKDIR /home/redpen  
RUN git clone http://github.com/recruit-tech/redpen.git  
WORKDIR /home/redpen/redpen  
RUN mvn install  
  
ADD scripts/init_service.sh /home/redpen/init_service.sh  
  
# start server  
EXPOSE 22 8080  
WORKDIR /home/redpen  
CMD sh ./init_service.sh && supervisord -c /etc/supervisord.conf  

