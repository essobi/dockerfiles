FROM python:3.6  
MAINTAINER Yohei Maeda <yohei.maeda.11@gmail.com>  
  
#RUN yum -y update && \  
# yum -y reinstall glibc-common && \  
# yum clean all  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends locales  
  
RUN echo en_US.UTF-8 UTF-8 > /etc/locale.gen  
RUN locale-gen  
RUN update-locale LANG=en_US.UTF-8  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV PYTHONIOENCODING=utf-8  
ARG DIR=/opt/app  
WORKDIR $DIR  
ADD ./requirements.txt ./  
  
RUN cat /etc/default/locale  
  
RUN pip install -r requirements.txt

