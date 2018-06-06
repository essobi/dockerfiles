# According to the cutadapt documentation, 3.5 appears to be the  
# latest supported Python 3 version.  
FROM python:3.5-slim  
MAINTAINER Vimalkumar Velayudhan <vimalkumarvelayudhan@gmail.com>  
  
ENV PYPI_VERSION 1.13  
RUN apt-get update && \  
apt-get install -y --no-install-recommends gcc libc6-dev && \  
pip install cutadapt==$PYPI_VERSION && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get purge -y --auto-remove gcc libc6-dev  
  
# create and set user for container  
RUN useradd -r -s /sbin/nologin cutadapt  
USER cutadapt  
  
ENTRYPOINT ["cutadapt"]  
CMD ["--help"]

