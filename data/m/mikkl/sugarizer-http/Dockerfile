FROM nginx:alpine  
RUN mkdir /sugarizer-repo  
WORKDIR /sugarizer-repo  
  
RUN apk update && apk upgrade && \  
apk add --no-cache bash git openssh  
  
RUN git clone https://github.com/llaske/sugarizer.git  
COPY nginx.conf /etc/nginx/nginx.conf  
RUN rm -fr sugarizer/.git

