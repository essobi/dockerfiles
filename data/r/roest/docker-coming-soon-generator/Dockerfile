FROM nginx  
  
# install dependencies  
RUN apt-get update && apt-get install -y \  
wget \  
git \  
php7.0-cli  
  
ENV BASE_DIR /usr/share/nginx/html  
WORKDIR $BASE_DIR  
  
ARG defaultTemplate="bootstrap4"  
ENV TEMPLATE=$defaultTemplate  
  
# remove nginx default content  
RUN rm /usr/share/nginx/html/*  
  
# add comming soon page  
ADD ./ $BASE_DIR  
  
RUN ./templates/bootstrap4/checkout.sh # can i do this dynamically?  
  
ADD compileAndRun.sh /usr/local/bin/  
  
ENTRYPOINT ["compileAndRun.sh"]

