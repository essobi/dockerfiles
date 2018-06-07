FROM python:2.7-slim-stretch  
  
ENV PHANTOMJS_FILENAME phantomjs-2.1.1-linux-x86_64.tar.bz2  
ENV PHANTOMJS_SOURCE
https://bitbucket.org/ariya/phantomjs/downloads/${PHANTOMJS_FILENAME}  
ENV PHANTOMJS_CHKSUM
"86dd9a4bf4aee45f1a84c9f61cf1947c1d6dce9b9e8d2a907105da7852460d2f"  
ADD fonts.txt /opt/  
RUN apt update && \  
apt install -y --no-install-recommends \  
bzip2 \  
curl \  
fontconfig \  
gcc \  
libcurl4-gnutls-dev \  
libgnutls28-dev \  
libssl-dev \  
\  
# multilingual support for phantomjs display  
$(cat /opt/fonts.txt)  
  
ADD requirements.txt /opt/  
RUN pip install requests && \  
pip install -r /opt/requirements.txt  
  
RUN curl -fssL ${PHANTOMJS_SOURCE} > ${PHANTOMJS_FILENAME} && \  
echo "${PHANTOMJS_CHKSUM} ${PHANTOMJS_FILENAME}" | sha256sum -c && \  
tar -C /usr/local/share -xjf /${PHANTOMJS_FILENAME} && \  
cp -vf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs \  
/usr/local/bin && \  
rm -rf /${PHANTOMJS_FILENAME} \  
/usr/local/share/phantomjs-2.1.1-linux-x86_64  
  
RUN mkdir -p /robot-scripts  
  
VOLUME ["/robot-scripts"]  
  
CMD ["/usr/local/bin/robot"]  

