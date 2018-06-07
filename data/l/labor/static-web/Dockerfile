# Debian Jessie  
FROM nginx  
MAINTAINER seu <seu@panopticon.re>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install \  
git-core \  
golang-go \  
ruby-i18n \  
build-essential \  
ruby-dev && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
RUN gem install jekyll jekyll-paginate  
  
# STATIC_SITE_(Name) = "(Hostname),(Git Repo),(Jekyll?)"  
ENV STATIC_SITE_STATIC="static.das-labor.org,https://github.com/das-
labor/static.das-labor.org.git,false"  
ENV STATIC_SITE_LT15="labortage.das-labor.org,https://github.com/das-
labor/lt15.git,false"  
ENV STATIC_SITE_REPAIRCAFE="repaircafe-bochum.de,https://github.com/das-
labor/repaircafe-bochum.de.git,true"  
ENV STATIC_SITE_BUNDESPOSCHT="bundesposcht.de,https://github.com/das-
labor/bundesposcht.de.git,false"  
# REDIRECT_SITE_(Name) = "(From),(To)"  
ENV REDIRECT_SITE_WWW_REPAIRCAFE="www.repaircafe-bochum.de,repaircafe-
bochum.de"  
COPY entrypoint.sh /  
COPY github_hook.go /  
CMD ["/entrypoint.sh"]  

