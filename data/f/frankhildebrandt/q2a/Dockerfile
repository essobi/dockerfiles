FROM frankhildebrandt/php-fpm  
  
RUN apt-get install -y git \  
&& docker-php-ext-install mysqli mbstring  
  
RUN git clone https://github.com/q2a/question2answer.git \  
&& git clone https://github.com/amiyasahu/Donut.git \  
&& git clone https://github.com/ganbox/qa-filter.git /question2answer/qa-
plugin/qa-filter \  
&& git clone https://github.com/NoahY/q2a-poll.git /question2answer/qa-
plugin/qa-poll \  
&& git clone https://github.com/svivian/q2a-user-activity-plus.git
/question2answer/qa-plugin/qa-user-activity \  
&& git clone https://github.com/NoahY/q2a-history.git /question2answer/qa-
plugin/qa-user-history \  
&& git clone https://github.com/NoahY/q2a-log-tags.git /question2answer/qa-
plugin/qa-log-tags \  
&& git clone https://github.com/dunse/qa-category-email-notifications.git
/question2answer/qa-plugin/qa-email-notification \  
&& git clone https://github.com/nakov/q2a-plugin-open-questions.git
/question2answer/qa-plugin/qa-questions-open  
  
COPY qa-config.php /question2answer/qa-config.php  
  
RUN rm -fR /var/www/html \  
&& ln -s /question2answer /var/www/html \  
&& ln -s /Donut/qa-plugin/Donut-admin /question2answer/qa-plugin \  
&& ln -s /Donut/qa-theme/Donut-theme /question2answer/qa-theme

