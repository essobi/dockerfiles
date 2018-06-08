FROM omarqazi/smick-baseimage:latest  
  
ENV HOME /root  
ENV RAILS_ENV production  
  
CMD ["/sbin/my_init"]  
RUN rm -f /etc/service/nginx/down  
RUN rm /etc/nginx/sites-enabled/default  
ADD config/webapp.conf /etc/nginx/sites-enabled/webapp.conf  
ADD config/postgres-env.conf /etc/nginx/main.d/postgres-env.conf  
ADD . /home/app/smickclub  
WORKDIR /home/app/smickclub  
RUN bundle install  
RUN rake assets:precompile  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN mkdir /etc/service/resque-worker  
ADD config/resque-worker.sh /etc/service/resque-worker/run  
RUN mkdir /etc/service/resque-scheduler  
ADD config/resque-scheduler.sh /etc/service/resque-scheduler/run  
EXPOSE 80

