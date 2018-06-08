FROM alpine  
RUN apk --no-cache add \  
perl \  
perl-dev \  
curl \  
wget \  
build-base \  
readline \  
readline-dev \  
ncurses-dev \  
&& curl -L https://cpanmin.us | perl - App::cpanminus \  
&& cpanm Devel::REPL -v \  
&& cpanm Term::ReadLine::Gnu -v \  
&& apk del \  
perl-dev \  
curl \  
wget \  
build-base \  
readline-dev \  
ncurses-dev  
CMD re.pl  

