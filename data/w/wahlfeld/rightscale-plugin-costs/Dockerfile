  
FROM alpine  
  
RUN apk update && \  
apk add --no-cache --upgrade \  
python \  
py2-requests  
  
COPY . /usr/local/rightscale-plugin-costs  
  
CMD ["crond", "-l", "2", "-f"]  

