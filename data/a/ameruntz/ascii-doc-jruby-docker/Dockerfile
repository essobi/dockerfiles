FROM azul/zulu-openjdk:8  
MAINTAINER Amer <amer@ictlab.com.ba>  
  
# Install wget  
RUN apt-get update && apt-get upgrade -y && apt-get -qqy install \  
wget \  
python3 \  
python3-pip \  
unzip \  
graphviz \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10
&& \  
update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 10  
  
# Set constants  
ENV JRUBY_VERSION 9.0.0.0.pre1  
ENV JRUBY_HOME /opt/jruby  
ENV PATH $JRUBY_HOME/bin:$PATH  
  
WORKDIR /opt  
# Download and extract jruby archive  
RUN wget -O -
https://s3.amazonaws.com/jruby.org/downloads/$JRUBY_VERSION/jruby-
bin-$JRUBY_VERSION.tar.gz \  
\--no-check-certificate | tar zxf - && \  
ln -s /opt/jruby-$JRUBY_VERSION ${JRUBY_HOME} && \  
find /opt/jruby-$JRUBY_VERSION -name "*.exe" -o -name "*.dll" -o -name "*.bat"
-print0 | xargs -0 rm -f  
  
# Install gems  
RUN jruby -S gem install asciidoctor asciidoctor-diagram coderay tilt slim
haml pry --no-ri --no-rdoc  
RUN pip install nwdiag blockdiag seqdiag actdiag blockdiagcontrib-cisco  
  
ENTRYPOINT ["asciidoctor"]  
CMD ["--help"]  
  
# ENV JRUBY_OPTS --2.0  

