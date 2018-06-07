FROM python:3.6.2  
MAINTAINER Helpful version: 0.1.3  
ADD https://cli.run.pivotal.io/stable?release=linux64-binary&source=github
/tmp/cf-cli.tgz  
RUN mkdir -p /usr/local/bin \  
&& tar -z -x -v -f /tmp/cf-cli.tgz -C /usr/local/bin \  
&& rm -f /tmp/cf-cli.tgz  
  
RUN (curl -fL https://getcli.jfrog.io | sh) \  
&& mv jfrog /usr/local/bin/  
  
# Install jq  
RUN cd /opt \  
&& mkdir jq \  
&& wget -O ./jq/jq http://stedolan.github.io/jq/download/linux64/jq \  
&& chmod +x ./jq/jq \  
&& ln -s /opt/jq/jq /usr/local/bin  
  
RUN echo "deb http://www.deb-multimedia.org jessie main non-free" >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y --force-yes dist-upgrade  
RUN apt-get install -y --force-yes ffmpeg  
RUN apt-get install -y --force-yes time  
ENTRYPOINT ["ffmpeg", "--help"]  

