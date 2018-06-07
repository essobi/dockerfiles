FROM python:3.6-stretch  
  
ENV TZ Asia/Tokyo  
ENV TINI_VERSION v0.17.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/local/sbin/tini  
RUN chmod +x /usr/local/sbin/tini  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install build-essential \  
gfortran \  
libatlas-base-dev \  
liblapack-dev \  
busybox-static  
  
RUN echo "${TZ}" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata  
  
RUN mkdir /elecwarn  
ADD . /elecwarn  
  
WORKDIR /elecwarn  
  
RUN pip install -r requirements.txt  
  
RUN mkdir -p /var/spool/cron/crontabs && \  
echo '*/10 1-23 * * * cd /elecwarn && python3 elecwarn.py' >>
/var/spool/cron/crontabs/root  
  
ENTRYPOINT ["/usr/local/sbin/tini", "--"]  
CMD ["busybox", "crond", "-f", "-L", "/dev/stderr"]  

