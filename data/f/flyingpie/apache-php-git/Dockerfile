FROM tutum/apache-php  
  
MAINTAINER Marco van den Oever <marco@flyingpie.nl>  
  
RUN apt-get update && apt-get install -y \  
git \  
ssh \  
supervisor  
  
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd
/var/log/supervisor  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN mkdir /git  
RUN mkdir /git/website.git  
RUN cd /git/website.git  
WORKDIR /git/website.git  
RUN git init --bare  
  
COPY ./post-receive /git/website.git/hooks/post-receive  
  
RUN chmod +x /git/website.git/hooks/post-receive  
  
RUN rm -r /app/*  
  
EXPOSE 22 80  
VOLUME /root/.ssh  
  
ENV ROOT_FOLDER /  
  
ADD ./run.sh /run.sh  
  
CMD ["sh", "/run.sh"]  

