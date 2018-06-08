FROM perl:5.20  
MAINTAINER Dan Burke <dburke@liquidweb.com>  
RUN apt-get clean && apt-get update && apt-get upgrade -y && apt-get clean  
RUN apt-get clean && apt-get update && apt-get install -y git vim telnet &&
apt-get clean  
  
RUN cpan -i Bundle::CPAN && rm -rf .cpan/build .cpan/Metadata .cpan/sources  
  
ADD Snapshot.pm /root/.cpan/Bundle/Snapshot.pm  
RUN cpan -i Bundle::Snapshot && rm -rf /root/.cpan/build /root/.cpan/Metadata
/root/.cpan/sources  
RUN cpanm -n Net::AMQP::RabbitMQ  
  
RUN mkdir -p /usr/local/lp/libs /usr/local/lp/git
/usr/local/lp/configs/LWConfig  
  
WORKDIR /usr/local/lp/git/doppler-dev  
  
CMD /bin/bash  
  

