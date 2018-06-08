FROM ubuntu:14.10  
ENV DEBIAN_FRONTEND noninteractive  
ENV TOMCAT_HOME /var/lib/tomcat7  
ENV NGINX_HOME /etc/nginx  
ENV FOODPEDIA_HOME /root/foodpedia/foodpedia-home  
  
RUN apt-get update  
RUN apt-get install -y tomcat7 git maven nginx wget unzip  
RUN apt-get clean  
  
WORKDIR /root  
  
RUN rm -rf $TOMCAT_HOME/webapps/*  
  
RUN git clone https://github.com/ailabitmo/foodpedia.git  
RUN cd $FOODPEDIA_HOME && mvn clean install -DskipTests=true  
RUN rm -rf /root/.m2/repository/*  
RUN cp $FOODPEDIA_HOME/target/*.war $TOMCAT_HOME/webapps/home.war  
  
RUN wget https://dl.dropboxusercontent.com/u/1497018/foodpedia/pubby.war  
RUN mkdir $TOMCAT_HOME/webapps/ROOT  
RUN unzip pubby.war -d $TOMCAT_HOME/webapps/ROOT/  
ADD config.ttl $TOMCAT_HOME/webapps/ROOT/WEB-INF/config.ttl  
  
RUN rm -rf $NGINX_HOME/sites-enabled/*  
RUN rm -rf $NGINX_HOME/sites-available/*  
ADD foodpedia.conf $NGINX_HOME/sites-available/foodpedia  
RUN ln -s $NGINX_HOME/sites-available/foodpedia $NGINX_HOME/sites-
enabled/foodpedia  
  
ADD start.sh /root/start.sh  
RUN chmod 777 /root/start.sh  
  
CMD ./start.sh  

