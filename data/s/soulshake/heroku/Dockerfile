FROM debian:jessie  
MAINTAINER AJ Bowen <aj@soulshake.net>  
  
RUN apt-get update && apt-get install -y \  
wget  
  
RUN apt-get install -y ruby  
  
#RUN wget --no-check-certificate -O- https://toolbelt.heroku.com/install-
ubuntu.sh | sh  
RUN echo "deb http://toolbelt.heroku.com/ubuntu ./" >
/etc/apt/sources.list.d/heroku.list  
RUN wget -O- https://toolbelt.heroku.com/apt/release.key | apt-key add -  
RUN apt-get update && apt-get install -y \  
heroku-toolbelt  
  
ENV PATH="/usr/local/heroku/bin:$PATH"  
# I guess we have to run this here to get past the initial download  
RUN heroku --help  
  
CMD ["--help"]  
ENTRYPOINT ["heroku"]  
  
# Heroku CLI Standalone  
# =====================  
# To install the standalone Heroku CLI:  
# $ xz -cd heroku-VERSION.tar.xz | tar -x  
# $ cd heroku  
# $ ./install  
# heroku installed to /usr/local/bin/heroku  

