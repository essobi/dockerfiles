FROM deepcase/sleuthkit:sleuthkit-4.4.2-patch02 as sleuth  
FROM ibmjava:9-sdk  
  
ENV JAVA_HOME=/opt/ibm/java  
  
RUN apt-get update \  
&& apt-get install -y --force-yes \  
git \  
mplayer2 \  
tesseract-ocr tesseract-ocr-por tesseract-ocr-osd \  
libparse-win32registry-perl \  
libesedb-utils \  
graphicsmagick \  
libmsiecf-utils \  
libpff1 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD http://mirror.nbtelecom.com.br/apache/maven/maven-3/3.5.2/binaries/apache-
maven-3.5.2-bin.tar.gz /opt/  
  
RUN tar xf /opt/apache-maven-3.5.2-bin.tar.gz -C /opt/  
RUN ln -s /opt/apache-maven-3.5.2/bin/mvn /bin/  
  
#creates .mplayer/config  
RUN mplayer  
  
COPY \--from=sleuth /usr/local/src/sleuthkit/sleuthkit.tar.gz /tmp/  
RUN tar xf /tmp/sleuthkit.tar.gz -C /  
RUN ldconfig  
  
WORKDIR /usr/local/src/iped/  
  
CMD /bin/bash  

