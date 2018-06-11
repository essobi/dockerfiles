FROM zfce/base-application:latest  
  
ENV DEV_MODE false  
ENV DATABASE_URL ''  
ENV REDIS_HOST 'redis'  
ENV REDIS_PORT '6379'  
ENV AWS_S3_VERSION 'latest'  
ENV AWS_S3_REGION 'ap-southeast-2'  
ENV AWS_S3_BUCKET 'villadbay'  
ENV AWS_ACCESS_KEY_ID 'AKIAJJJOH43PYYUNHUDQ'  
ENV AWS_SECRET_ACCESS_KEY ''  
ENV APP_ENV 'prod'  
ENV APP_DEBUG 'false'  
ENV IMAGE_CDN ''  
# CUSTOM SOFTWARE REQS  
RUN  apt-get update && \  
apt-get install -y libmagickwand-dev \--no-install-recommends && \  
apt-get install -y jq awscli  && \  
pecl install imagick && \  
docker-php-ext-enable imagick  
  
# Create custom PHP settings  
RUN echo "ZGF0ZS50aW1lem9uZSA9IEF1c3RyYWxpYS9CcmlzYmFuZQ==" | base64 \--decode
>> /usr/local/etc/php/conf.d/custom.ini && \  
# EDIT vhost  
echo
"PFZpcnR1YWxIb3N0ICo6ODA+DQoNCiAgICBEb2N1bWVudFJvb3QgL3Zhci93d3cvaHRtbA0KICAgIDxEaXJlY3RvcnkgL3Zhci93d3cvaHRtbD4NCiAgICAgICAgQWxsb3dPdmVycmlkZSBOb25lDQogICAgICAgIE9yZGVyIEFsbG93LERlbnkNCiAgICAgICAgQWxsb3cgZnJvbSBBbGwNCg0KICAgICAgICA8SWZNb2R1bGUgbW9kX3Jld3JpdGUuYz4NCiAgICAgICAgICAgIE9wdGlvbnMgLU11bHRpVmlld3MNCiAgICAgICAgICAgIFJld3JpdGVFbmdpbmUgT24NCiAgICAgICAgICAgIFJld3JpdGVDb25kICV7UkVRVUVTVF9GSUxFTkFNRX0gIS1mDQogICAgICAgICAgICBSZXdyaXRlUnVsZSBeKC4qKSQgaW5kZXgucGhwIFtRU0EsTF0NCiAgICAgICAgPC9JZk1vZHVsZT4NCiAgICA8L0RpcmVjdG9yeT4NCg0KICAgICMgdW5jb21tZW50IHRoZSBmb2xsb3dpbmcgbGluZXMgaWYgeW91IGluc3RhbGwgYXNzZXRzIGFzIHN5bWxpbmtzDQogICAgIyBvciBydW4gaW50byBwcm9ibGVtcyB3aGVuIGNvbXBpbGluZyBMRVNTL1Nhc3MvQ29mZmVlU2NyaXB0IGFzc2V0cw0KICAgICMgPERpcmVjdG9yeSAvdmFyL3d3dy9wcm9qZWN0Pg0KICAgICMgICAgIE9wdGlvbnMgRm9sbG93U3ltbGlua3MNCiAgICAjIDwvRGlyZWN0b3J5Pg0KDQogICAgIyBvcHRpb25hbGx5IGRpc2FibGUgdGhlIFJld3JpdGVFbmdpbmUgZm9yIHRoZSBhc3NldCBkaXJlY3Rvcmllcw0KICAgICMgd2hpY2ggd2lsbCBhbGxvdyBhcGFjaGUgdG8gc2ltcGx5IHJlcGx5IHdpdGggYSA0MDQgd2hlbiBmaWxlcyBhcmUNCiAgICAjIG5vdCBmb3VuZCBpbnN0ZWFkIG9mIHBhc3NpbmcgdGhlIHJlcXVlc3QgaW50byB0aGUgZnVsbCBzeW1mb255IHN0YWNrDQogICAgPERpcmVjdG9yeSAvdmFyL3d3dy9odG1sL2J1bmRsZXM+DQogICAgICAgIDxJZk1vZHVsZSBtb2RfcmV3cml0ZS5jPg0KICAgICAgICAgICAgUmV3cml0ZUVuZ2luZSBPZmYNCiAgICAgICAgPC9JZk1vZHVsZT4NCiAgICA8L0RpcmVjdG9yeT4NCiAgICBFcnJvckxvZyAgJHtBUEFDSEVfTE9HX0RJUn0vZXJyb3IubG9nDQogICAgQ3VzdG9tTG9nICR7QVBBQ0hFX0xPR19ESVJ9L2FjY2Vzcy5sb2cgY29tYmluZWQNCjwvVmlydHVhbEhvc3Q+"
| base64 \--decode > /etc/apache2/sites-enabled/000-default.conf && \  
# EDIT TimeZone (through dpkg)  
ln -fs /usr/share/zoneinfo/Australia/Brisbane /etc/localtime && \  
dpkg-reconfigure -f noninteractive tzdata && \  
rm -rf /var/www/html  
  
WORKDIR /var/www  
  
COPY . /var/www  
  
RUN chown -R deployuser:deploygroup /var/www  
  
# Change owner to avoid running as root  
USER deployuser  
  
# RUN COMPOSER to generate parameters.yml file  
RUN /usr/local/bin/php -r "copy('https://getcomposer.org/installer',
'composer-setup.php');" && \  
/usr/local/bin/php -r "copy('https://composer.github.io/installer.sig',
'composer-installer.sig');" && \  
/usr/local/bin/php -r "if (hash_file('SHA384', 'composer-setup.php') ===
trim(file_get_contents('composer-installer.sig'))) { echo 'Installer
verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); }
echo PHP_EOL;" && \  
/usr/local/bin/php composer-setup.php && \  
/usr/local/bin/php -r "unlink('composer-setup.php');" && \  
/usr/local/bin/php -r "unlink('composer-installer.sig');" && \  
/usr/local/bin/php composer.phar update -n  
  
  
RUN GIT_CHANGES=$( \  
git status -s \  
) && \  
if [ ${#GIT_CHANGES} -gt 0 ]; then \  
# We now commit updated files from composer  
echo $GIT_CHANGES && \  
ssh-keygen -t rsa -N "" -b 4096 -C "mark1979smith@googlemail.com" -f
/home/deployuser/.ssh/id_rsa && \  
eval "$(ssh-agent -s)" && \  
ssh-add /home/deployuser/.ssh/id_rsa && \  
ssh-keyscan ssh.github.com >> /home/deployuser/.ssh/known_hosts && \  
# Create Deployment Key  
printf "%s" '{"title": "Villa DBay Deploy Key (Write) ' > /tmp/.create-
deployment-key.json && \  
printf "%s" "$(echo `date`)" >> /tmp/.create-deployment-key.json && \  
printf "%s" '", "key":"' >> /tmp/.create-deployment-key.json && \  
printf "%s" "$(cat /home/deployuser/.ssh/id_rsa.pub | tee)" >> /tmp/.create-
deployment-key.json && \  
printf "%s" '", "read_only": false}' >> /tmp/.create-deployment-key.json && \  
# Send Deplooyment Key  
CURRENT_DEPLOYMENT_KEY_URL=$( \  
curl -X POST -H "$(cat /tmp/.git.token)" -d "$(cat /tmp/.create-deployment-
key.json)" https://api.github.com/repos/mark1979smith/villadbay/keys | jq
'.url' | sed s/\"//g \  
) && \  
# Ensure we are up to date when debugging  
git fetch && git pull && \  
# Config Settings  
git config user.email "hosting@marksmith.email" && \  
git config user.name "Mark Smith" && \  
git config push.default "simple" && \  
# Change Remote from HTTP to SSH  
git remote rm origin && \  
git remote add origin git@ssh.github.com:mark1979smith/villadbay.git && \  
# Add All Files, Commit then Push  
git add -A && \  
git commit -m "[AUTO] Updates to composer installation" && \  
git push -u origin \--all && \  
# Remove Deployment Key  
echo "Removing Deployment Key: $CURRENT_DEPLOYMENT_KEY_URL" && \  
curl -X DELETE -H "$(cat /tmp/.git.token)" $CURRENT_DEPLOYMENT_KEY_URL && \  
rm -f /tmp/.create-deployment-key.json && \  
rm -f /tmp/.git.token; \  
fi  
  
# Switch back to ROOT  
USER root  

