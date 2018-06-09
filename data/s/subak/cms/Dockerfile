FROM subak/cms:base  
MAINTAINER Subak Systems <info@subak.jp>  
  
RUN mkdir -m 700 -p .ssh \  
&& echo "Host github.com\n\tStrictHostKeyChecking no\n" > .ssh/config \  
&& echo "Host bitbucket.org\n\tStrictHostKeyChecking no\n" >> .ssh/config  
  
RUN git clone https://github.com/subak/cms_app_web.git web \  
&& git clone https://github.com/subak/cms_app_blog.git blog  
  
COPY h2o.yml h2o.conf  
COPY cms-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["cms-entrypoint.sh"]

