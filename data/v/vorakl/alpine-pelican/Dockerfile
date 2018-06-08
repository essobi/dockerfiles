FROM vorakl/alpine:latest  
  
MAINTAINER "Oleksii Tsvietnov" <me@vorakl.name>  
  
RUN apk add --no-cache python3  
RUN pip3 install --upgrade pip && \  
pip3 install pelican pelican-minify pelican-youtube markdown beautifulsoup4  
  
CMD ["pelican", "-h"]  

