FROM ubuntu  
  
RUN locale-gen en_US en_US.UTF-8 && \  
dpkg-reconfigure locales  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ant \  
curl \  
git \  
libgtk2.0-0 \  
libxtst-dev \  
openssh-client \  
wget \  
xvfb \  
openjdk-8-jdk \  
openjfx  
  
RUN java -version  
  
ENV JRUBY_VERSION 9.1.5.0  
RUN wget https://s3.amazonaws.com/jruby.org/downloads/${JRUBY_VERSION}/jruby-
bin-${JRUBY_VERSION}.tar.gz -O /tmp/jruby.tar.gz  
RUN mkdir /opt/jruby \  
&& tar -zx --strip-components=1 -f /tmp/jruby.tar.gz -C /opt/jruby \  
&& rm /tmp/jruby.tar.gz \  
&& update-alternatives --install /usr/local/bin/ruby ruby /opt/jruby/bin/jruby
1  
ENV PATH /opt/jruby/bin:$PATH  
  
RUN echo 'gem: --no-rdoc --no-ri' >> ~/.gemrc  
  
RUN gem install bundler  
  
ADD .deploy/xvfb_init /etc/init.d/xvfb  
RUN chmod a+x /etc/init.d/xvfb  

