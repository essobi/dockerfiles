# Dockerfile for static site generator Pelican, written in Python
http://docs.getpelican.com  
FROM python:2  
MAINTAINER Alexey Rubtsov  
  
ENV REFRESHED_AT 2014-11-29  
ENV BLOG_DIR /root/myblog  
  
RUN apt-get update && apt-get -y install python-pip git  
RUN pip install pelican Markdown  
  
RUN git clone https://github.com/Vostbur/diary.git $BLOG_DIR  
WORKDIR $BLOG_DIR  
RUN mkdir output  
RUN pelican content  
WORKDIR $BLOG_DIR/output  
  
EXPOSE 8000  
# CMD bash -c "pelican-quickstart -p $BLOG_DIR"  
# CMD ["/bin/bash"]  
CMD python -m SimpleHTTPServer  

