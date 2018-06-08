FROM lucidfrontier45/python-uwsgi:3-alpine  
MAINTAINER Tommy Kelly <docker@tkel.ly>  
  
ENV sourceDir /flask-youtube-metadata  
  
RUN apk update && apk upgrade && \  
apk add --no-cache bash git openssh  
  
RUN git clone https://github.com/tomkel/flask-youtube-metadata.git $sourceDir  
  
WORKDIR $sourceDir  
  
RUN pip3 install -r requirements.txt  
  
ENTRYPOINT ["uwsgi", "--socket", ":5000", "--module", "youtube:app", \  
"--master", "--die-on-term", "--vacuum", "--manage-script-name", \  
"--stats", ":1717"]  
CMD ["--processes", "4", "--threads", "2"]  
  
EXPOSE 5000 1717  

