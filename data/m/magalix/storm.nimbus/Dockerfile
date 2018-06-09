FROM magalix/storm.base  
  
MAINTAINER Mohamed Ahmed <Mohamed.Ahmed@Magalix.com>  
ADD test.jar /  
ADD start.sh /  
ADD conf.sh /  
ADD 2014_Gaz_counties_national.txt /  
ADD geoinfo.csv /  
ADD udacity-storm-hack-0.0.1-SNAPSHOT-jar-with-dependencies.jar /  
#ADD udacity-storm-lesson2_stage7-0.0.1-SNAPSHOT-jar-with-dependencies.jar /  
EXPOSE 3772 6627  
WORKDIR /opt/apache-storm  
  
ENTRYPOINT ["/start.sh"]  
#  

