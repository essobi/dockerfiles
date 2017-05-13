FROM ubuntu:xenial
MAINTAINER Anatoly Litovsky <anatolylit@gmail.com>
MAINTAINER Anna Litovsky <anna.makhlina@mail.huji.ac.il>
ENV container docker

RUN apt-get clean && apt-get update
RUN apt-get install -y python python-pip unzip wget
RUN pip install numpy
RUN pip install QIIME

COPY SilvaDb/Silva_123_release.zip /root/Silva_123_release.zip
RUN cd root && unzip /root/Silva_123_release.zip && rm /root/Silva_123_release.zip

COPY SilvaDb/Silva.gold.bacteria.zip /root/Silva.gold.bacteria.zip
RUN cd root && unzip /root/Silva.gold.bacteria.zip && rm /root/Silva.gold.bacteria.zip

COPY Mothur.linux_64.zip /root/Mothur.linux_64.zip
RUN cd root && unzip /root/Mothur.linux_64.zip && rm /root/Mothur.linux_64.zip

COPY SilvaDb/silva_lanemask_mothur.txt /root/silva_lanemask_mothur.txt

RUN apt-get install -y python-tk
