FROM ubuntu:14.04  
  
RUN apt-get -y update  
  
RUN apt-get install -y language-pack-ko  
  
# set locale ko_KR  
RUN locale-gen ko_KR.UTF-8  
  
ENV LANG ko_KR.UTF-8  
ENV LANGUAGE ko_KR.UTF-8  
ENV LC_ALL ko_KR.UTF-8  
  
#set time seoul  
RUN mv /etc/localtime /etc/localimte_origin  
RUN ln -s /usr/share/zoneinfo/Asia/Seoul /etc/localtime  
  
#install JDK8  
RUN apt-get purge openjdk*  
  
RUN apt-get install -y software-properties-common  
  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java8-installer  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# install or set nginx  
RUN apt-get install -y nginx  
  
RUN rm -f /etc/nginx/sites-available/default  
#RUN rm -f /etc/nginx/nginx.conf  
ADD conf/default /etc/nginx/sites-available/  
ADD conf/aircomix.conf /etc/nginx/sites-enabled/  
  
VOLUME ["/var/comix","/var/novel","/var/www/","/var/script"]  
  
ADD script/start.sh /var/script/  
RUN chmod 755 /var/script/start.sh  
  
#ADD ./www /var/www/  
  
EXPOSE 80  
EXPOSE 31257  
EXPOSE 31357  
EXPOSE 31000  
  
#CMD ["sh","-c","/var/script/start.sh"]

