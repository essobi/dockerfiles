# VERSION 0.1  
# DOCKER-VERSION 0.10.0  
# AUTHOR Saulo Alves <sauloal@gmail.com>  
# DESCRIPTION  
# TO BUILD docker build -t sauloal/mongoapi .  
# TO RUN docker run -d -p 27022:22 -p 27017:27017 -p 28017:28017 -p
27080:27080 --name="sauloal_mongoapi" sauloal/mongoapi  
# TO UPLOAD while true; do docker push sauloal/mongoapi; echo $?; if [ $? ==
"0" ]; then exit 0; fi; done  
  
#FROM robinvdvleuten/mongo  
FROM sauloal/mongo  
  
MAINTAINER Saulo Alves <sauloal@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
#ENV DEBIAN_PRIORITY critical  
#ENV DEBCONF_NOWARNINGS yes  
  
#https://gist.github.com/jpetazzo/6127116  
## this forces dpkg not to call sync() after package extraction and speeds up
install  
#RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup  
## we don't need and apt cache in a container  
#RUN echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache  
  
#RUN apt-get update  
  
RUN apt-get install -y python-setuptools build-essential git python-dev; apt-
get clean all  
  
RUN easy_install pymongo pip  
  
RUN git clone https://github.com/10gen-labs/sleepy.mongoose.git  
  
#RUN apt-get remove python-setuptools build-essential git python-dev  
  
#mongo port  
EXPOSE 27017  
  
#mongo rest port  
EXPOSE 28017  
  
#mongoose port  
EXPOSE 27080  
  
#ssh port  
EXPOSE 22  
  
ADD mongoose.service.conf /etc/supervisor/conf.d/mongoose.service.conf  
ADD run.sh /run.sh  
  
CMD /bin/bash /run.sh  
  
#ENTRYPOINT /usr/sbin/sshd; /usr/bin/nohup /usr/bin/python
sleepy.mongoose/httpd.py --xorigin & \ ; disown $? ; /usr/bin/nohup
/usr/bin/mongod --rest  
  
#ENTRYPOINT ["bash"]  

