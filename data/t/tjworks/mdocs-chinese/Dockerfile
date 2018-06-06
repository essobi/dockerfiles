FROM ubuntu:14.04  
MAINTAINER TJ Tang "jianfa.tang@mognodb.com"  
RUN apt-get update  
RUN apt-get install -y git curl python  
RUN apt-get install -y python-sphinx python-yaml python-argparse inkscape
python-pip  
RUN pip install giza  
RUN apt-get install -y python droopy fabric  
  
RUN mkdir -p /opt/mongo-docs  
WORKDIR /opt/mongo-docs  
  
ENV TESTENV TESTVAL  
ADD etc/sitecustomize.py /etc/python2.7/sitecustomize.py  
ADD etc/setup.sh /opt/setup.sh  
  
CMD ["/bin/bash"]  
#ENTRYPOINT ["/bin/bash"]  
##### Build ####  
# docker build --rm=true -t tjworks/mongo-docs .  
##### Local test run ###  
# docker run -i -v /home/docker/osx/docs:/opt/mongo-docs -t tjworks/mongo-docs  
#### init  
# git clone https://github.com/tjworks/docs  
# python bootstrap.py  
#### Install ###  
# install docker  
# docker run -i -t tjworks/mongo-docs -v /home/docker/osx/mongo-
docs:/opt/mongo-docs /opt/setup.sh  
# docker run -i -t tjworks/mongo-docs -v /home/docker/osx/mongo-
docs:/opt/mongo-docs  

