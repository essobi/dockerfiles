FROM lsiobase/alpine.python  
MAINTAINER rix1337  
  
RUN git clone https://github.com/Fjodor42/jottalib-ng && \  
cd jottalib-ng && \  
python setup.py install && \  
cd / && \  
rm -rf /jottalib-ng  
  
COPY root/ /  
  
ENV JOTTACLOUD_USERNAME yourusername  
ENV JOTTACLOUD_PASSWORD yourpassword  
  
VOLUME /sync  

