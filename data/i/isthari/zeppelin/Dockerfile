FROM isthari/java-7-base  
  
RUN apt-get update  
RUN apt-get install -y r-base wget  
RUN cd /root; wget
http://apache.uvigo.es/zeppelin/zeppelin-0.6.2/zeppelin-0.6.2-bin-all.tgz  
RUN cd /root; tar -xzf zeppelin-0.6.2-bin-all.tgz  
RUN rm /root/zeppelin-0.6.2-bin-all.tgz  
RUN mv /root/zeppelin-0.6.2-bin-all /opt/zeppelin  
  
RUN R -e "install.packages('knitr', repos = 'http://cran.us.r-project.org')"  
RUN R -e "install.packages('devtools', repos =
'http://cran.us.r-project.org')"  
RUN R -e "install.packages('ggplot2', repos = 'http://cran.us.r-project.org')"  
  
RUN R -e "install.packages('mplot', repos = 'http://cran.us.r-project.org')"  
RUN R -e "install.packages('googleVis', repos =
'http://cran.us.r-project.org')"  
  
# not working  
#RUN R -e "library(devtools); install_github('ramnathv/rCharts')"  
RUN R -e "install.packages('gimnet', repos = 'http://cran.us.r-project.org')"  
RUN R -e "install.packages('pROC', repos = 'http://cran.us.r-project.org')"  
RUN R -e "install.packages('data.table', repos =
'http://cran.us.r-project.org')"  
RUN R -e "install.packages('caret', repos = 'http://cran.us.r-project.org')"  
RUN R -e "install.packages('sqldf', repos = 'http://cran.us.r-project.org')"  
RUN R -e "install.packages('wordcloud', repos =
'http://cran.us.r-project.org')"  
  
ADD start.sh /opt/zeppelin  
ADD interpreter.json /opt/zeppelin/conf/interpreter.json  
RUN chmod oug+x //opt/zeppelin/start.sh  
  
EXPOSE 8080  
CMD /opt/zeppelin/start.sh  
  

