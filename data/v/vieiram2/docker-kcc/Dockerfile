FROM debian:stretch  
MAINTAINER Rafael Mendes  
  
# Install dependencies  
RUN echo 'deb http://deb.debian.org/debian stretch non-free' >>
/etc/apt/sources.list.d/stretch.non-free.list \  
&& apt-get update \  
&& apt-get install -y python3 python3-dev python3-pip libpng-dev libjpeg-dev
p7zip-full unrar \  
git ssh wget \  
&& yes | pip3 install --upgrade pillow python-slugify psutil pyqt5 raven  
  
# Download Kindle Comic Converter (KCC)  
ENV KCC_PATH "/tools/kcc"  
ENV KCC_VERSION "5.4.1"  
RUN mkdir -p ${KCC_PATH} \  
&& git clone \--branch ${KCC_VERSION} https://github.com/ciromattia/kcc.git
${KCC_PATH} \  
&& chmod +x ${KCC_PATH}/kcc-c2e.py  
ENV PATH "${KCC_PATH}:${PATH}"  
# Download KindleGen  
RUN wget -O /tmp/kindlegen.tar.gz
"http://kindlegen.s3.amazonaws.com/kindlegen_linux_2.6_i386_v2_9.tar.gz" \  
&& tar zxvf /tmp/kindlegen.tar.gz -C ${KCC_PATH}  
  
# Cleanup  
RUN apt-get clean -y \  
&& apt-get autoclean -y \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR ${KCC_PATH}  
CMD ["kcc-c2e.py"]  

