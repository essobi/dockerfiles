FROM python:3.6-alpine  
MAINTAINER Rick Peters <rick.peters@me.com>  
  
# install graphviz  
RUN apk add --no-cache graphviz  
  
# essential template resource not available in development build  
# issue registered with mkdocs contributor  
# ADD search-results-template.mustache /usr/local/lib/python3.5/site-
packages/mkdocs/assets/search/mkdocs/js/  
# install mkdocs  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY requirements.txt /usr/src/app/  
RUN pip install --no-cache-dir -r requirements.txt  
  
#ONBUILD COPY . /usr/src/app  
# add markdown extension  
ADD mdx_graphviz.py /usr/local/lib/python3.6/site-
packages/markdown/extensions/  
  
# make application directory available as volume  
VOLUME /usr/src/app  
  
# Alpine has no localization suppoert in the musl library apparantly, we get
warnings but no errors so igonore for now  
#ENV LANG C.UTF-8  
ENV TZ Europe/Amsterdam  
# since we use it as development container, default action is a shell  
CMD [ "/bin/bash" ]  

