  
# docker run -t -i -p 8080:8080 -p 9001:9001 -v /Users/eric/Desktop/Test:/home
emilletfr/domo-server-vapor-docker  
#FROM emilletfr/swift-docker:swift-3.0.2-release  
FROM swift:4.0  
MAINTAINER Eric Millet <emilletfr@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
USER root  
  
RUN mkdir /root/.vapor  
RUN cd /root/.vapor && mkdir /domo-server-vapor  
ADD . /root/.vapor/domo-server-vapor  
WORKDIR /root/.vapor/domo-server-vapor  
RUN swift build  
CMD ["./.build/debug/App"]  
  
# Standard Supervisor port  
#EXPOSE 9001  
# Standard SSH port  
#EXPOSE 22  
# Add user jenkins to the image.  
#RUN adduser --quiet jenkins  
# Set password for the jenkins user (you may want to alter this).  
#RUN echo "jenkins:jenkins" | chpasswd  
# Allow the jenkins user to update the system.  
#RUN echo "jenkins ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/jenkins  
# Set up sshd.  
#RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd  
#RUN mkdir -p /var/run/sshd  
#RUN cd /home/jenkins && git clone https://github.com/emilletfr/domo-server-
vapor.git  
#RUN cd /home/jenkins/domo-server-vapor && swift build  
# Add App & sshd to supervisor  
#COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
#launch supervisor added service at docker startup  
#CMD ["/usr/bin/supervisord"]  

