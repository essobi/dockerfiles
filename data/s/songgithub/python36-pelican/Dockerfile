# find the most slim py 3.6 package  
FROM python:3.6.5-alpine3.7  
# this is for Pelican - a static website generator  
RUN pip install pelican Markdown  
# install bash as I love it too  
RUN apk add \--update bash && rm -rf /var/cache/apk/*

