FROM debian:stretch-slim  
MAINTAINER Mattias Wadman mattias.wadman@gmail.com  
  
ENV DROPBOX_FOLDER="site"  
ENV HOME=/app  
ENV LC_ALL="en_US.UTF-8"  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get -y install wget locales nginx && \  
apt-get clean  
  
# make sure utf-8 works in filenames etc  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen  
RUN locale-gen  
  
RUN mkdir /app  
WORKDIR /app  
  
RUN \  
wget -O - "https://github.com/krallin/tini/releases/download/v0.16.1/tini" >
/usr/local/bin/tini && \  
chmod a+x /usr/local/bin/tini && \  
wget -O -
"https://github.com/cortesi/modd/releases/download/v0.4/modd-0.4-linux64.tgz"
| tar xfz - && \  
mv modd-0.4-linux64/modd /usr/local/bin && \  
rm -rf tmp && \  
wget -O -
"https://github.com/spf13/hugo/releases/download/v0.27/hugo_0.27_Linux-64bit.tar.gz"
| tar xfz - hugo && \  
mv hugo /usr/local/bin/hugo && \  
rm -rf hugo_0.27_linux_amd64 && \  
wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf - -C
/app  
  
RUN mkdir -p /app/.dropbox /app/Dropbox  
COPY run_hugo nginx.conf modd.conf /app/  
RUN chown -R nobody:nogroup /app  
  
USER nobody  
  
VOLUME ["/app/.dropbox", "/app/Dropbox"]  
EXPOSE 8080  
CMD ["/usr/local/bin/tini", "--", "/usr/local/bin/modd"]  

