FROM alpine:3.4  
#  
# install dependencies  
#  
# install packages  
RUN apk add --update \  
wget \  
git \  
python \  
python-dev \  
py-pip \  
build-base \  
curl \  
&& pip install virtualenv \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /app  
  
ADD requirements.txt .  
RUN virtualenv /env && /env/bin/pip install -r /app/requirements.txt  
  
#  
# install adb ( code from sorccu/adbd )  
#  
# Set up insecure default key  
RUN mkdir -m 0750 /root/.android  
ADD files/insecure_shared_adbkey /root/.android/adbkey  
ADD files/insecure_shared_adbkey.pub /root/.android/adbkey.pub  
ADD files/update-platform-tools.sh /usr/local/bin/update-platform-tools.sh  
  
RUN set -xeo pipefail && \  
apk update && \  
apk add wget ca-certificates tini && \  
wget -O "/etc/apk/keys/sgerrand.rsa.pub" \  
"https://raw.githubusercontent.com/andyshinn/alpine-pkg-
glibc/master/sgerrand.rsa.pub" && \  
wget -O "/tmp/glibc.apk" \  
"https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.23-r3/glibc-2.23-r3.apk" && \  
wget -O "/tmp/glibc-bin.apk" \  
"https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.23-r3/glibc-
bin-2.23-r3.apk" && \  
apk add "/tmp/glibc.apk" "/tmp/glibc-bin.apk" && \  
rm "/etc/apk/keys/sgerrand.rsa.pub" && \  
rm "/root/.wget-hsts" && \  
rm "/tmp/glibc.apk" "/tmp/glibc-bin.apk" && \  
rm -r /var/cache/apk/APKINDEX.* && \  
/usr/local/bin/update-platform-tools.sh  
  
# Expose default ADB port  
#EXPOSE 5037  
# Set up PATH  
ENV PATH $PATH:/opt/platform-tools  
  
  
  
#  
# install restop-devices  
#  
WORKDIR /usr/local/lib  
  
# install restop-core  
RUN git clone
https://cocoon_bitbucket@bitbucket.org/cocoon_bitbucket/wbackend.git restop  
RUN mv restop/restop-client/restop_client restop/restop_client  
#RUN git clone https://github.com/coleifer/walrus.git walrus  
#RUN mv walrus/walrus restop/walrus  
ENV PYTHONPATH=/usr/local/lib/restop  
  
  
#CMD ["/env/bin/python", "app.py]  
CMD ["ash"]

