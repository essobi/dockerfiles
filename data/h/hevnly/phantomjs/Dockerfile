FROM phusion/baseimage  
  
ENV PHANTOMJS phantomjs-2.1.1-linux-x86_64  
  
RUN apt-get update -y  
  
RUN apt-get install -y \  
build-essential chrpath libssl-dev libxft-dev \  
libfreetype6 libfreetype6-dev \  
libfontconfig1 libfontconfig1-dev \  
zip git  
  
RUN ln -s /usr/bin/python3 /usr/bin/python  
  
# Install phantomjs  
WORKDIR /tmp/  
ADD https://cnpmjs.org/mirrors/phantomjs/${PHANTOMJS}.tar.bz2
${PHANTOMJS}.tar.bz2  
RUN tar xvjf ${PHANTOMJS}.tar.bz2 && \  
mv $PHANTOMJS /usr/local/share && \  
ln -sf /usr/local/share/$PHANTOMJS/bin/phantomjs /usr/local/bin  
  
# Install node  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - && \  
apt-get install -y nodejs  
  
# Install AWS  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" && \  
unzip awscli-bundle.zip && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
  
# Clean up temp dir  
RUN rm -rf /tmp/*  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

