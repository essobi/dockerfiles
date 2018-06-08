FROM fedora:21  
MAINTAINER Michal Jurosz <mj@mj41.cz>  
  
RUN yum makecache fast  
  
# Install man pages  
RUN sed -i '/nodocs/d' /etc/yum.conf  
RUN yum update -y  
  
RUN yum install -y man tar gzip unzip git make curl tree diffutils gcc \  
perl perl-Test-Simple perl-ExtUtils-MakeMaker perl-App-cpanminus \  
perl-autodie perl-File-Slurp perl-Text-Markdown perl-HTML-Parser perl-File-
ShareDir  
  
RUN cpanm HTML::FromANSI  
  
RUN useradd --uid 1000 -U linus  
USER linus  
ENV HOME /home/linus  
  
RUN mkdir -p /home/linus/prbuilder/third-part/  
WORKDIR /home/linus/prbuilder/third-part/  
  
RUN git clone https://github.com/hakimel/reveal.js.git  
  
RUN git clone https://github.com/mj41/Presentation-Builder.git Presentation-
Builder  
ENV PERL5LIB /home/linus/prbuilder/third-part/Presentation-
Builder/lib:$PER5LIB  
  
# Update base image  
WORKDIR /home/linus/prbuilder/third-part/reveal.js/  
RUN echo "Force Docker image rebuild of reveal.js to particular revision." \  
&& git fetch && git reset --hard 3.1.0 \  
&& git log -n1 --oneline HEAD  
  
WORKDIR /home/linus/prbuilder/third-part/Presentation-Builder/  
RUN echo "Force Docker image rebuild of Presentation-Builder to particular
revision." \  
&& git fetch && git reset --hard 6deb8b4 \  
&& git log -n1 --oneline HEAD  
  
ADD docker-bin/ /home/linus/prbuilder/docker-bin/  
  
WORKDIR /home/linus/prbuilder/  
CMD /bin/sh  

