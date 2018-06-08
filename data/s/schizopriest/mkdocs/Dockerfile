FROM alpine  
MAINTAINER Pascal Reeb <pascal at reeb dot io>  
  
RUN apk add --update \  
python \  
py-pip  
RUN pip install mkdocs  
RUN pip install Markdown==2.6.7  
RUN pip install mkdocs-pandoc  
RUN rm -rf /var/cache/apk/*  

