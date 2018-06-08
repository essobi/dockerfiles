FROM python:3.6-slim-stretch  
MAINTAINER Holger Schinzel <holger@dash.org>  
  
RUN apt-get update && \  
apt-get install git curl mysql-client cython3 -y && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ARG SENTINEL_COMMIT=f2f3c3a76591c66101b3221610db7a279c01468f  
  
RUN git clone https://github.com/polispay/sentinel.git /sentinel && \  
cd /sentinel && \  
git checkout $SENTINEL_COMMIT && \  
rm sentinel.conf && \  
rm -rf .git && \  
pip install -r requirements.txt && exit 0  
  
ENV HOME /sentinel  
WORKDIR /sentinel  
  
ADD run.sh /  
  
CMD /run.sh  

