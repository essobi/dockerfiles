FROM elasticsearch:5.3.0-alpine  
MAINTAINER Jonathan Roizin <joroizin@gmail.com>  
  
# install hspell data files,  
# hebmorph requirement  
ENV HEBMORPH_VERSION 5.3.0  
ENV HEBMORPH_FILE hebmorph-lucene-$HEBMORPH_VERSION  
ENV ELASTICSEARCH_ANALYSIS_HEBREW_VERSION 5.3.0  
RUN apk add --update --no-cache sudo  
RUN echo '%root ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/root  
RUN addgroup elasticsearch root  
  
COPY hspell-data-files /var/lib/hspell-data-files  
  
# install hebmorph plugin  
RUN elasticsearch-plugin install --verbose
https://bintray.com/synhershko/elasticsearch-analysis-
hebrew/download_file?file_path=elasticsearch-analysis-
hebrew-$ELASTICSEARCH_ANALYSIS_HEBREW_VERSION.zip  
  

