# Floreant POS Dockerfile  
#  
# https://github.com/genome21/Floreantpos-1  
#  
FROM centos:centos7  
MAINTAINER Robert Wilkins III <thecainvestors@gmail.com>  
  
# Install  
RUN yum -y update; yum clean all  
RUN yum -y install git; yum clean all  
RUN yum -y epel-release; yum clean all  
RUN yum -y install x11vnc xterm tigervnc-server xorg-x11-server-Xvfb
xorg-x11-twm xorg-x11-font dejavu-sans-fonts dejavu-serif-fonts xdotool; yum
clean all  
RUN yum -y install java-1.7.0-openjdk; yum clean all  
RUN yum -y install java-1.7.0-openjdk-devel; yum clean all  
  
# Add the xstartup file into the image  
ADD ./xstartup /  
  
RUN mkdir /.vnc  
RUN \cp -f ./xstartup /.vnc/.  
RUN chmod -v +x /.vnc/xstartup  
  
EXPOSE 5901  
CMD ["vncserver", "-fg" ]  
# ENTRYPOINT ["vncserver", "-fg" ]  
# Define working directory.  
WORKDIR /usr/Downloads  
  
# Clone the git repo to the docker container  
RUN git clone https://github.com/genome21/floreantpos-1.git  
  
# Run Floreant POS  
RUN ls  
RUN ls floreantpos-1  
RUN ls floreantpos-1/lib

