FROM ubuntu  
MAINTAINER Pini Reznik "p.reznik@uglyduckling.nl"  
RUN echo deb http://archive.ubuntu.com/ubuntu precise universe >>
/etc/apt/sources.list  
RUN apt-get update  
  
RUN apt-get install -y less sshpass vim inetutils-ping python2.7 python-
software-properties python-setuptools ssh openssh-server build-essential
python-crypto python-dev  
  
RUN mkdir /var/run/sshd  
RUN echo 'root:ansible' |chpasswd  
  
RUN easy_install pip  
RUN pip install ansible  
  
# Set locale (fix the locale warnings)  
RUN localedef -v -c -i en_US -f UTF-8 en_US.UTF-8 || :  
  
# Copy the files into the container  
ADD . /src  
  
EXPOSE 22  
CMD ["/bin/bash", "/src/startup.sh"]  
  

