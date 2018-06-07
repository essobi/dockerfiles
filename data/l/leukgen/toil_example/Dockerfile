FROM python:2.7-jessie  
  
RUN \  
# install packages dependencies  
apt-get update -yqq && \  
apt-get install -yqq \  
curl \  
git \  
locales \  
python-pip \  
wget && \  
apt-get clean && \  
\  
# configure locale, see https://github.com/rocker-org/rocker/issues/19  
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \  
locale-gen en_US.utf8 && \  
/usr/sbin/update-locale LANG=en_US.UTF-8  
# set locales  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
# mount the output volume as persistant  
ENV OUTPUT_DIR /data  
VOLUME ${OUTPUT_DIR}  
  
# install toil_example  
COPY . /code  
RUN pip install /code && rm -rf /code  
  
# add entry point  
ENTRYPOINT ["toil_example"]  

