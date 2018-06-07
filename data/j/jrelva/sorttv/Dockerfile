FROM phusion/baseimage  
MAINTAINER Jason Kingsbury  
  
RUN apt-get -q update  
  
RUN (echo y;echo y)|cpan; mkdir /opt/sorttv; apt-get -y -q install make build-
essential libxml-sax-expat-perl  
RUN cpan File::Copy::Recursive File::Glob LWP::Simple TVDB::API Getopt::Long
Switch WWW::TheMovieDB XML::Simple JSON::Parse  
  
VOLUME ["/data/movies"]  
VOLUME ["/data/tvshows"]  
VOLUME ["/data/incoming"]  
  
ADD sorttv/sorttv.pl /opt/sorttv/  
ADD sorttv/sorttv.conf /opt/sorttv/  
ADD sortd /opt/sorttv/  
  
CMD ["/opt/sorttv/sortd"]  
  

