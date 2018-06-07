FROM phusion/passenger-ruby22  
MAINTAINER Oleksandr Simonov <oleksandr@simonov.me>  
ENV HOME /root  
ENV SERVE_STATIC_ASSETS false  
RUN sudo -u app -H git clone https://github.com/errbit/errbit.git
/home/app/errbit  
WORKDIR /home/app/errbit  
RUN sudo -u app -H bundle install --deployment  
RUN sudo -u app -H bundle exec rake assets:precompile RAILS_ENV=production
SERVE_STATIC_ASSETS=false  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN rm -f /etc/service/nginx/down  
RUN rm /etc/nginx/sites-enabled/default  
COPY errbit.conf /etc/nginx/sites-enabled/errbit.conf  
COPY errbit-env.conf /etc/nginx/main.d/errbit-env.conf  
COPY errbit.cron /etc/cron.d/errbit  
CMD ["/sbin/my_init"]  

