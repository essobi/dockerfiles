FROM alpine:3.4  
MAINTAINER Stewart V. Wright <stewart@vifortech.com>  
  
RUN apk add --update \  
ca-certificates \  
curl \  
file \  
git \  
nano \  
wget \  
python \  
py-pip \  
python3 \  
&& rm -rf /var/cache/apk/*  
  
# Install the msmtp-queue and offlineimap (+ six)  
RUN pip3 install --upgrade pip \  
&& pip3 install mir.msmtpq \  
&& pip2 install six \  
&& pip2 install offlineimap  
  
ADD msmtp.FAKE /bin/msmtp  
RUN chmod a+rx /bin/msmtp  
  
RUN adduser -S mymail  
WORKDIR /home/mymail  
USER mymail  
  
RUN mkdir /home/mymail/bin  
ENV USER mymail  
ENV HOME /home/mymail  
ENV PATH /home/mymail/bin:${PATH}  
  
# Install the Gmail OAuth2 tools and send.py  
RUN cd ~ \  
&& git clone https://github.com/google/gmail-oauth2-tools \  
&& git clone https://github.com/cscorley/send.py.git \  
&& cd bin && ln -s ~/send.py/send.py  
  
ADD scripts /scripts  
ENV PATH /home/mymail/bin:/scripts:${PATH}  

