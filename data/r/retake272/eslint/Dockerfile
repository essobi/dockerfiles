FROM node  
  
MAINTAINER "Matsuura Keita<retake272@gmail.com>"  
# locale  
RUN apt-get update  
RUN apt-get install locales -y  
RUN echo "ja_JP UTF-8" > /etc/locale.gen  
RUN locale-gen  
  
ENV LANG ja_JP.UTF-8  
ENV LANGUAGE ja_JP.UTF-8  
ENV LC_ALL ja_JP.UTF-8  
ARG eslint_version=4.19.1  
RUN npm install -g eslint@${eslint_version}  
  
WORKDIR /app  
VOLUME /app  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  

