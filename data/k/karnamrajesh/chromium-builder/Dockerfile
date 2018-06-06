FROM mhart/alpine-node:8  
MAINTAINER Rajesh Karnam  
  
RUN apk add --no-cache python3 bc git libexif udev chromium chromium-
chromedriver xvfb ttf-freefont curl bash  
RUN python3 -m pip install boto3  
  
ENV CHROME_BIN chromium-browser  

