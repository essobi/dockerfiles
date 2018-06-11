FROM ubuntu:16.04  
# APT-GET Installs  
RUN \  
apt-get update && \  
\  
echo "Installing Tools..." && \  
DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \  
apt-transport-https \  
libterm-readline-perl-perl \  
locales \  
mc \  
openjdk-8-jre \  
python-setuptools \  
vim \  
wget \  
&& \  
\  
echo "Installing Postfix..." && \  
echo "postfix postfix/main_mailer_type string Internet site" > preseed.txt &&
\  
debconf-set-selections preseed.txt && \  
DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -q -y \  
postfix \  
&& \  
\  
echo "Installing dumb-init..." && \  
wget -qO /usr/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 && \  
chmod +x /usr/bin/dumb-init && \  
\  
echo "Installing Supervisor..." && \  
easy_install supervisor && \  
\  
echo "Cleaning up..." && \  
rm preseed.txt && \  
rm -r /var/lib/apt/lists/*  
  
# Define stable version to install  
ENV ZAMMAD_VERSION=2.2.0  
# APT-GET Installs from 3rd party repos  
RUN \  
echo "Configuring Repos and Keys..." && \  
wget -qO- https://dl.packager.io/srv/zammad/zammad/key | apt-key add - && \  
wget -O /etc/apt/sources.list.d/zammad.list
https://dl.packager.io/srv/zammad/zammad/stable/installer/ubuntu/16.04.repo &&
\  
\  
apt-get update && \  
\  
echo "Installing Zammad..." && \  
DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \  
zammad=$ZAMMAD_VERSION\\* \  
&& \  
initctl stop nginx && \  
initctl stop zammad && \  
\  
echo "Cleaning up..." && \  
rm -r /var/lib/apt/lists/*  
  
# Configure Nginx  
# Change localhost to 127.0.0.1 (http://serverfault.com/a/529403)  
RUN \  
sed -i -e 's/server localhost/server 127.0.0.1/' /etc/nginx/sites-
available/zammad.conf && \  
\  
rm -rf /etc/nginx/sites-enabled/default  
# Forward logs to docker log collector  
RUN \  
sed -i -e 's/^.*config\\.logger.*$/ config.logger =
ActiveSupport::TaggedLogging.new(Logger.new(STDOUT))/'
/opt/zammad/config/environments/production.rb && \  
sed -i -e 's/ \$stdout/ #\$stdout/' /opt/zammad/script/*.rb && \  
sed -i -e 's/ \$stderr/ #\$stderr/' /opt/zammad/script/*.rb && \  
\  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log && \  
ln -sf /dev/stdout /var/log/nginx/zammad.access.log && \  
ln -sf /dev/stderr /var/log/nginx/zammad.error.log  
  
# Copy config  
ADD config/database.yml /opt/zammad/config/database.yml  
ADD config/supervisord.conf /etc/supervisord.conf  
  
# Copy scripts  
ADD scripts/docker-entrypoint.sh /docker-entrypoint.sh  
  
# Set config and scripts permissions  
RUN \  
chmod 744 /*.sh && \  
\  
chmod 644 /opt/zammad/config/database.yml && \  
chown zammad:zammad /opt/zammad/config/database.yml  
  
# Some source modifications (the worst way to do this, I know)  
RUN \  
echo "Mod: Don't set font in emails, use default font" && \  
sed -i -e 's/html_email_css_font = "[^"]*"/html_email_css_font = ""/'
/opt/zammad/config/initializers/html_email_style.rb && \  
\  
echo "Fix: Allow to paste links into editor (#464)" && \  
sed -i -e "s/html\\.find('a, font/html\\.find('font/"
/opt/zammad/app/assets/javascripts/app/lib/app_post/utils.coffee && \  
sed -i -e "s/@mapTagAttributes:/@mapTagAttributes:\\\n 'A': ['href']/"
/opt/zammad/app/assets/javascripts/app/lib/app_post/utils.coffee && \  
sed -i -e 's/t\\.find("a, font/t\\.find("font/'
/opt/zammad/public/assets/application-*.js && \  
sed -i -e 's/mapTagAttributes=./mapTagAttributes={A:["href"],/'
/opt/zammad/public/assets/application-*.js && \  
\  
echo "Fix: Do not convert simple links in articles" && \  
sed -i -e "s/\\(url_same?(node\\['href'\\], node.text)\\)/\1 \&\&
node.text.include?('\/\/')/" /opt/zammad/lib/html_sanitizer.rb && \  
\  
echo "Mod: [form_submit] Add product data to body" && \  
sed -i -e "s/body: params\\[:body\\]/body: params[:product_name].present? ?
\"[#{params[:product_name]} #{params[:version]} | #{params[:os]} |
#{params[:country]} | #{params[:reason]}]\\\\\n\\\\\n#{params[:body]}\" :
params[:body]/" /opt/zammad/app/controllers/form_controller.rb && \  
\  
echo "Mod: [form_submit] Fail silently on honeypot field submission" && \  
sed -i -e "s/\\(# validate input\\)/if params[:req_name] \\\&\\\&
!params[:req_name].empty?\\\n render json: {}, status: :ok\\\n return\\\n
end\\\n\\\n \1/" /opt/zammad/app/controllers/form_controller.rb  
  
# Define environment variables for DB connection  
ENV \  
RAILS_ENV=production \  
PATH=/opt/zammad/bin:$PATH \  
GEM_PATH=/opt/zammad/vendor/bundle/ruby/2.4.0/ \  
\  
DB_ADAPTER=mysql2 \  
DB_DATABASE=zammad \  
DB_USERNAME=zammad \  
DB_PASSWORD="" \  
DB_HOST=mysql \  
DB_PORT=3306 \  
DB_CREATE=false \  
DB_MIGRATE=false \  
DB_INDEX=false \  
\  
ES_URL=http://elasticsearch:9200  
  
# Expose ports  
EXPOSE 80 3000 6042 9001 9200  
  
# WORKDIR for Zammad  
WORKDIR "/opt/zammad"  
  
# ENTRYPOINT and CMD  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["supervisord", "-c", "/etc/supervisord.conf"]  

