# ciphrtxt-test  
FROM ubuntu:16.04  
# TODO: Put the maintainer name in the image metadata  
MAINTAINER Joseph deBlaquiere <jadeblaquiere@yahoo.com>  
  
# TODO: Rename the builder environment variable to inform users about
application you provide them  
ENV BUILDER_VERSION 0.1  
# TODO: Install required packages here:  
RUN apt-get update -y && apt-get upgrade -y && apt-get install git python3
python3-pip golang-1.6 libleveldb1v5 libleveldb-dev -y  
#RUN yum install -y leveldb leveldb-devel && yum clean all -y  
RUN echo "installing python components via pip..."  
RUN pip3 install tornado requests requests_futures plyvel pycrypto  
RUN pip3 install git+https://github.com/jadeblaquiere/ecpy.git  
RUN pip3 install git+https://github.com/jadeblaquiere/ciphrtxt-lib.git  
RUN pip3 install git+https://github.com/jadeblaquiere/python-ctcoinlib.git  
  
# TODO (optional): Copy the builder files into /opt/app-root  
# COPY ./<builder_folder>/ /opt/app-root/  
# TODO: Copy the S2I scripts to /usr/libexec/s2i, since openshift/base-centos7
image sets io.openshift.s2i.scripts-url label that way, or update that label  
# COPY ./.s2i/bin/ /usr/libexec/s2i  
# TODO: Drop the root user and make the content of /opt/app-root owned by user
1001  
# RUN chown -R 1001:1001 /opt/app-root  
# create a non-priv user  
RUN useradd --create-home --user-group --uid 1001 ciphrtxt  
USER 1001  
# TODO: Set the default CMD for the image  
# CMD ["usage"]  
ENV GOPATH /home/ciphrtxt  
  
#install ctcd  
ENV PATH /usr/lib/go-1.6/bin:$PATH  
  
#CMD /bin/sh  

