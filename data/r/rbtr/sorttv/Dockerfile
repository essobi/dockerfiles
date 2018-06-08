FROM perl:5.24.2  
RUN apt-get update \  
&& apt-get install -y unzip  
WORKDIR /  
RUN curl -O
https://pilotfiber.dl.sourceforge.net/project/sorttv/SortTV1.37.zip  
RUN unzip SortTV1.37.zip  
WORKDIR /sorttv  
RUN cpan File::Copy::Recursive File::Glob LWP::Simple TVDB::API Getopt::Long
Switch WWW::TheMovieDB JSON::Parse XML::Simple  
CMD perl sorttv.pl  

