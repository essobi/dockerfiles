#  
# Bedework quickstart dockerfile  
#  
# Run with:  
# #docker run -p 8080:8080 bedework  
# #firefox http://localhost:8080/bedework  
#  
# Further setup instructions here
https://wiki.jasig.org/display/BWK310/Running+Bedework  
#  
FROM java:8  
MAINTAINER robipolli@gmail.com  
RUN apt-get update && apt-get -y install supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN wget http://dev.bedework.org/downloads/3.10.3/quickstart-3.10.3.zip -O
/quickstart-3.10.3.zip \  
&& unzip /quickstart-3.10.3.zip -x "*/*/.svn/*" \  
&& rm /quickstart-3.10.3.zip  
  
RUN mv /quickstart-3.10.3 /bedework  
WORKDIR /bedework  
  
# Setup configuration before supervisord starts bw.  
RUN bash bw deployConf  
  
EXPOSE 8080  
CMD ["/usr/bin/supervisord"]  

