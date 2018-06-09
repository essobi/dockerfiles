FROM python:3.6  
MAINTAINER Ted Liefeld <jliefeld@cloud.ucsd.edu>  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
COPY common/container_scripts/runS3OnBatch.sh /usr/local/bin/runS3OnBatch.sh  
COPY common/container_scripts/runLocal.sh /usr/local/bin/runLocal.sh  
RUN chmod ugo+x /usr/local/bin/runS3OnBatch.sh && \  
chmod ugo+x /usr/local/bin/runLocal.sh  
  
RUN mkdir /build  
  
ADD requirements.txt /build/requirements.txt  
RUN pip install -r /build/requirements.txt  
RUN pip install awscli  
  
CMD [ "/usr/local/bin/runS3OnBatch.sh"]  

