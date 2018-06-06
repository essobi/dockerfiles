FROM phusion/passenger-ruby18  
  
WORKDIR /home/app  
ENV HOME /home/app  
  
RUN apt-get update; \  
apt-get install --force-yes -y libxml2 libxml2-dev libxslt1-dev libxslt1.1 &&
\  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN git config --global user.email "blambeau@gmail.com" && \  
git config --global user.name "Bernard Lambeau"  
  
RUN touch /root/.ssh/known_hosts && \  
ssh-keyscan github.com >> /root/.ssh/known_hosts  
  
RUN cd /tmp && \  
git clone -q https://github.com/chefbe-dot-net/classandjazz.git && \  
rm -rf /home/app/ && \  
mv /tmp/classandjazz /home/app  
  
RUN rm /etc/nginx/sites-enabled/default && \  
rm -f /etc/service/nginx/down && \  
cp /home/app/config/webapp.conf /etc/nginx/sites-enabled/webapp.conf  
  
RUN cd /home/app && \  
bundle install && \  
chown app.app $HOME -R  
  
CMD ["/sbin/my_init"]  

