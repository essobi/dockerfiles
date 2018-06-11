FROM ubuntu:14.04  
# Configuring locales  
ENV DEBIAN_FRONTEND noninteractive  
RUN dpkg-reconfigure locales && locale-gen en_US.UTF-8 && update-locale
LANG=en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update && apt-get install -y -q \  
git-core \  
git \  
curl  
  
RUN mkdir -p /app  
WORKDIR /app  
  
# Install NodeJS  
RUN curl
https://nodejs.org/download/release/v0.10.41/node-v0.10.41-linux-x64.tar.gz|
tar -zxf - --strip-components=1 -C /usr  
  
# Setup git  
RUN git config --global user.email spocksplanet@gmail.com  
RUN git config --global user.name "Volkan Unsal"  
  
# Install statsd  
RUN git clone https://github.com/etsy/statsd.git /app/statsd  
  
# Install the cloudwatch backend  
RUN cd /app/statsd && npm install aws-cloudwatch-statsd-backend  
  
# Copy the setup over  
COPY ./app/* /app/  
  
RUN groupadd -r statsd && useradd -r -g statsd statsd  
  
USER statsd  
EXPOSE 8125/udp  
EXPOSE 8126  
ENTRYPOINT ["node"]  
CMD ["/app/statsd/stats.js", "/app/config.js"]  
  

