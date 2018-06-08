FROM python:alpine3.7  
ADD . /uppoder/src  
  
WORKDIR /uppoder/src  
  
RUN pip install -e .  
  
VOLUME ["/podcasts", "/upodder"]  
  
CMD ["upodder", "--podcastdir", "/podcasts", "--basedir", "/upodder", "--
filename-format", "{feed_title}/{entry_title}.{filename_extension}"]  

