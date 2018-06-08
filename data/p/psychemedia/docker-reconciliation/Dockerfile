FROM ubuntu:trusty  
  
MAINTAINER tony.hirst@gmail.com  
  
RUN apt-get update -y  
RUN apt-get upgrade -y  
  
RUN apt-get install -y openjdk-7-jre-headless  
  
#RUN wget http://okfnlabs.org/reconcile-csv/#download  
  
ADD addfile.sh /addfile.sh  
RUN chmod 755 /addfile.sh  
  
ADD reconcile-csv-0.1.1.jar reconcile-csv-0.1.1.jar  
ADD UK-MPs.csv /tmp/import/UK-MPs.csv  
  
ENV RECONFILE UK-MPs.csv  
ENV SEARCHCOL FullTitle  
ENV IDCOL Member_Id  
  
  
EXPOSE 8000  
#java -jar reconcile-csv-0.1.1.jar <CSV-File> <Search Column> <ID Column>  
#CMD ["java", "-jar", "reconcile-csv-0.1.1.jar","UK-MPs.csv",
"FullTitle","Member_Id"]  
CMD /addfile.sh && java -jar reconcile-csv-0.1.1.jar /data/$RECONFILE
$SEARCHCOL $IDCOL  

