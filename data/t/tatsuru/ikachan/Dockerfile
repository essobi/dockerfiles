FROM debian  
MAINTAINER Tatsuru Watanabe <w.tatsuru@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y build-essential curl libssl-dev  
  
RUN curl -s https://raw.githubusercontent.com/tagomoris/xbuild/master/perl-
install > /tmp/perl-install  
RUN bash /tmp/perl-install 5.18.2 /opt/perl-5.18  
  
ENV PATH /opt/perl-5.18/bin:$PATH  
RUN cpanm App::Ikachan  
  
EXPOSE 4979  
#ENTRYPOINT ikachan -o 0.0.0.0 -S chat.freenode.net  
RUN ikachan --help || true  

