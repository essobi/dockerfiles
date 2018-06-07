FROM ubuntu:14.04  
MAINTAINER Yunbo WANG <iyunbo@iyunbo.org>  
  
# setup environnement  
ENV GATLING_HOME /var/lib/gatling  
ENV USER_BIN /usr/local/bin  
RUN mkdir -p $GATLING_HOME  
RUN addgroup -q gatling  
RUN adduser -q --home $GATLING_HOME \--shell /bin/bash --ingroup gatling
gatling  
ENV USER_BIN /usr/local/bin  
RUN echo 'root:performance' |chpasswd  
RUN echo 'gatling:gatling' |chpasswd  
RUN mkdir -p /var/run/sshd  
RUN chown -R gatling:gatling $GATLING_HOME  
  
# install necessary software  
RUN apt-get update  
RUN apt-get install -q -y wget zip vim openssh-server git supervisor
openjdk-7-jdk && apt-get clean  
  
# install gatling  
ADD
https://oss.sonatype.org/content/repositories/snapshots/io/gatling/highcharts/gatling-
charts-highcharts/2.0.0-SNAPSHOT/gatling-charts-highcharts-2.0.0-SNAPSHOT-
bundle.zip $GATLING_HOME/  
RUN unzip $GATLING_HOME/*.zip -d $GATLING_HOME/  
RUN mv $GATLING_HOME/gatling-charts-highcharts-2.0.0-SNAPSHOT
$GATLING_HOME/gatling  
RUN rm $GATLING_HOME/*.zip  
ADD gatling.conf $GATLING_HOME/gatling/conf/gatling.conf  
ADD perf $GATLING_HOME/gatling/user-files/simulations/  
  
# install supervisor  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# update permisions  
RUN chown -R gatling:gatling $GATLING_HOME  
RUN chmod -R 777 /tmp  
  
# public ports  
EXPOSE 22  
CMD ["/usr/bin/supervisord"]  

