#FROM ubuntu:14.04  
FROM frvi/ruby  
  
MAINTAINER mezz64 <jtmihalic@gmail.com>  
  
# build environment settings  
#ENV DEBIAN_FRONTEND noninteractive  
  
# install packages for dashing  
RUN apt-get update && \  
# apt-get install software-properties-common -y --no-install-recommends && \  
# apt-add-repository ppa:brightbox/ruby-ng && \  
# apt-get update && \  
# apt-get install -y --no-install-recommends build-essential ruby2.1
ruby2.1-dev python3-pip git node nodejs libsqlite3-dev postgresql-server-
dev-9.3 libpq-dev sqlite && \  
apt-get install -y --no-install-recommends build-essential python3-pip git
node nodejs libsqlite3-dev postgresql-server-dev-9.4 libpq-dev sqlite && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install dashing and bundle  
RUN gem install dashing --no-rdoc --no-ri && \  
gem install bundle --no-rdoc --no-ri && \  
gem install execjs --no-rdoc --no-ri  
  
# add hapush python helpers  
RUN pip3 install daemonize sseclient configobj && \  
pip3 install --upgrade requests  
  
#RUN mkdir /dashing && \  
# dashing new dashing && \  
# cd /dashing && \  
# bundle && \  
# ln -s /dashing/dashboards /dashboards && \  
# ln -s /dashing/jobs /jobs && \  
# ln -s /dashing/assets /assets && \  
# ln -s /dashing/lib /lib-dashing && \  
# ln -s /dashing/public /public && \  
# ln -s /dashing/widgets /widgets && \  
# mkdir /dashing/config && \  
# mv /dashing/config.ru /dashing/config/config.ru && \  
# ln -s /dashing/config/config.ru /dashing/config.ru && \  
# ln -s /dashing/config /config  
  
# Clone hadashboard repository to get bundle gems  
RUN git clone https://github.com/acockburn/hadashboard.git && \  
cd /hadashboard && \  
bundle && \  
cd /  
  
COPY files/start.sh /  
  
#VOLUME ["/dashboards", "/jobs", "/lib-dashing", "/config", "/public",
"/widgets", "/assets"]  
  
  
VOLUME /config  
  
# Clone hadashboard repository  
#RUN git clone https://github.com/acockburn/hadashboard.git && \  
# ln -s /hadashboard /config  
  
# expose ports  
EXPOSE 3030  
  
# Change to hadashboard working directory  
WORKDIR /config  
  
#ENTRYPOINT ["dashing"]  
#CMD ["start", "-p", "3030"]  
CMD ["/start.sh"]  

