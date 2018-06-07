FROM hearstat/alpine-ruby  
  
MAINTAINER HearstAutomation Team <atat@hearst.com>  
  
ENV DASHING_HOME /dashing  
ENV PORT 3030  
ENV SHELL /bin/bash  
  
RUN gem install bundle dashing  
RUN mkdir $DASHING_HOME && \  
dashing new dashing && \  
cd $DASHING_HOME && bundle && \  
mkdir $DASHING_HOME/config && \  
mv $DASHING_HOME/config.ru $DASHING_HOME/config/config.ru && \  
ln -s $DASHING_HOME/config/config.ru $DASHING_HOME/config.ru && \  
rm -rf $DASHING_HOME/dashboards/* $DASHING_HOME/jobs/*  
  
COPY dashing.sh /usr/bin/dashinit  
COPY widget-install.rb $DASHING_HOME/  
COPY widgets.yml $DASHING_HOME/  
COPY Gemfile $DASHING_HOME/  
COPY dashboards/dashboard.erb $DASHING_HOME/dashboards/  
COPY dashboards/layout.erb $DASHING_HOME/dashboards/  
COPY config/dashing.conf $DASHING_HOME/config/  
  
## Upgrade to font awesome 4.5  
COPY font-awesome/fonts/fontawesome-webfont.eot
$DASHING_HOME/assets/fonts/fontawesome-webfont.eot  
COPY font-awesome/fonts/fontawesome-webfont.svg
$DASHING_HOME/assets/fonts/fontawesome-webfont.svg  
COPY font-awesome/fonts/fontawesome-webfont.ttf
$DASHING_HOME/assets/fonts/fontawesome-webfont.ttf  
COPY font-awesome/fonts/fontawesome-webfont.woff
$DASHING_HOME/assets/fonts/fontawesome-webfont.woff  
COPY font-awesome/fonts/fontawesome-webfont.woff2
$DASHING_HOME/assets/fonts/fontawesome-webfont.woff2  
COPY font-awesome/fonts/FontAwesome.otf
$DASHING_HOME/assets/fonts/FontAwesome.otf  
COPY font-awesome/stylesheets/font-awesome.css
$DASHING_HOME/assets/stylesheets/font-awesome.css  
  
VOLUME ["$DASHING_HOME/dashboards/", "$DASHING_HOME/jobs/",
"$DASHING_HOME/config/", "$DASHING_HOME/public/", "$DASHING_HOME/widgets/"]  
  
EXPOSE $PORT  
WORKDIR $DASHING_HOME  
  
CMD ["/usr/bin/dashinit"]  

