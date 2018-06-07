FROM bitnami/redmine:latest  
  
RUN dpkg --get-selections | awk '{ print $1 }' > /dpkg.list.origin &&\  
apt-get update &&\  
apt-get install -y wget build-essential libmysqlclient-dev libpq-dev
libmagickwand-dev &&\  
dpkg --get-selections | awk '{ print $1 }' > /dpkg.list.install &&\  
cat /dpkg.list.origin | while read line; do sed -i "/$line/d"
/dpkg.list.install; done &&\  
cd /opt/bitnami/redmine &&\  
git clone https://github.com/alexbevi/redmine_knowledgebase.git
plugins/redmine_knowledgebase &&\  
git clone https://github.com/peclik/clipboard_image_paste.git
plugins/clipboard_image_paste &&\  
git clone https://github.com/eckucukoglu/redmine-reminder-emails.git
plugins/reminderemails &&\  
git clone https://github.com/Restream/redmine_custom_reports.git
plugins/redmine_custom_reports &&\  
bundle install --no-deployment &&\  
bundle clean --force &&\  
wget https://oss-
binaries.phusionpassenger.com/binaries/passenger/by_release/5.1.4/agent-x86_64-linux.tar.gz
&&\  
tar zxf agent-x86_64-linux.tar.gz -C /usr/bin &&\  
apt-get autoremove -y --purge $(cat /dpkg.list.install) &&\  
apt-get autoremove -y --purge $(dpkg --get-selections | awk '{ print $1 }' |
grep .*-dev) &&\  
apt-get clean all &&\  
apt-get autoclean &&\  
rm -f agent-x86_64-linux.tar.gz /dpkg.list.origin /dpkg.list.install  

