FROM ruby:2.4-alpine  
  
RUN apk update && apk add build-base nodejs gmp-dev openssl  
RUN apk add openssh openrc && rc-update add sshd && ssh-keygen -t rsa -f
/etc/ssh/ssh_host_rsa_key  
  
RUN mkdir /app  
WORKDIR /app  
  
COPY ./Gemfile ./Gemfile.lock ./  
RUN bundle install --binstubs  
  
RUN adduser sshuser -D  
RUN echo 'sshuser:mypass2' | chpasswd  
  
COPY . .  
  
#RUN chmod +x startup.sh  
RUN rake assets:precompile  
  
EXPOSE 443  
EXPOSE 80  
EXPOSE 3000  
#CMD ["rails", "server", "-b", "0.0.0.0", "-e", "production"]  
#CMD ["rails", "server", "-b", "0.0.0.0", "-e", "development"]  
#CMD /usr/sbin/sshd && rails server -b 0.0.0.0 -e development  
CMD /usr/sbin/sshd && puma -C config/puma.rb -e development

