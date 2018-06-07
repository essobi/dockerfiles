# Unide landing page dockerfile  
# docker run -d --name docs -p 4567 \  
# -e GOOGLE_ANALYTICS_ID="" \  
# hivetech/intuition-doc  
FROM phusion/passenger-ruby20  
MAINTAINER Xavier Bruhiere, <xavier.bruhiere@gmail.com>  
  
# Install okdoc and it's dependencies  
RUN apt-get update && \  
apt-get install -y git-core python python-pip && \  
git clone \--depth 1 https://github.com/hackliff/okdoc.git && \  
cd okdoc && python setup.py install  
  
# Get articles and generate documentation  
#ADD . /tmp/intuition-doc  
RUN git clone \--depth 1 https://github.com/intuition-io/doc.git
/tmp/intuition-doc  
RUN okdoc build --from /tmp/intuition-doc --to /opt/middleman-app  
  
WORKDIR /opt/middleman-app  
RUN echo gem \"rack-contrib\" >> Gemfile && \  
echo gem \"unicorn\" >> Gemfile && \  
echo gem \"newrelic_rpm\" >> Gemfile && \  
bundle install && \  
bundle exec middleman build  
  
CMD bundle exec unicorn -p 4567 config.ru  
EXPOSE 4567  

