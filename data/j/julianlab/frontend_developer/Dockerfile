# Version: 0.0.1  
FROM ruby:latest  
MAINTAINER Julian Labuschagne "personxx@gmail.com"  
ENV REFRESHED_AT 2016-12-09  
RUN apt-get update -yqq && \  
apt-get upgrade -yqq && \  
apt-get install -y curl git locales && \  
curl -OL https://github.com/Yelp/dumb-init/releases/download/v1.0.1/dumb-
init_1.0.1_amd64.deb && \  
dpkg -i dumb-init_1.0.1_amd64.deb && rm dumb-init_1.0.1_amd64.deb  
  
RUN dpkg-reconfigure locales && \  
locale-gen C.UTF-8 && \  
/usr/sbin/update-locale LANG=C.UTF-8  
  
# Install needed default locale for Makefly  
RUN echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen && \  
locale-gen  
  
# Install Software  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - && \  
apt-get install -y nodejs && \  
npm install -g bower grunt-cli gulp-cli foundation-cli  
  
# Install Hugo  
RUN curl -o /opt/hugo.tar.gz -SL
"https://github.com/spf13/hugo/releases/download/v0.15/hugo_0.15_linux_$(dpkg
--print-architecture).tar.gz" && \  
cd /opt/ && tar -zxvf hugo.tar.gz && \  
cp /opt/hugo_0.15_linux_amd64/hugo_0.15_linux_amd64 /usr/local/bin/hugo  
  
# Install Jekyll  
RUN gem install jekyll && \  
gem install octopress-paginate  
  
# Create a non privileged user  
RUN useradd -ms /bin/bash frontend  
  
# Set default locale for the environment  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
# USER frontend  
VOLUME /home/frontend  
WORKDIR /home/frontend  
ENV TERM=linux  
  
EXPOSE 4000  
EXPOSE 9000  
EXPOSE 1313  
EXPOSE 35729  
CMD ["/bin/bash"]  

