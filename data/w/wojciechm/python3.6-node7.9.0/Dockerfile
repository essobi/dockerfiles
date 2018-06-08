From debian:sid  
  
RUN apt-get update && \  
apt-get install -y python3.6 python3-pip python3.6-dev build-essential libssl-
dev libffi-dev python-virtualenv curl git xvfb wget zip tar firefox chromium \  
openssh-client rsync postgresql-9.6  
  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash &&
\  
wget https://chromedriver.storage.googleapis.com/2.30/chromedriver_linux64.zip
&& \  
wget
https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-linux64.tar.gz
&& \  
unzip chromedriver_linux64.zip && \  
tar xzf geckodriver-v0.17.0-linux64.tar.gz && \  
mv chromedriver /usr/local/bin/ && \  
mv geckodriver /usr/local/bin/ && \  
export NVM_DIR="$HOME/.nvm" && \  
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && \  
nvm install 7.9.0 && \  
nvm use 7.9.0  
  
RUN service postgresql start && \  
su \- postgres -c "createuser tester --login" && \  
su \- postgres -c "createdb testing --owner tester" && \  
su \- postgres -c "psql --dbname testing -c \"ALTER SCHEMA public OWNER TO
tester\"" && \  
su \- postgres -c "psql -c \"ALTER USER tester WITH PASSWORD 'T35t3r'\"" && \  
sed -i "/local all postgres peer/ i local all tester md5"
/etc/postgresql/9.6/main/pg_hba.conf && \  
sed -i "/local all postgres peer/ i host all tester 127.0.0.1/32 md5"
/etc/postgresql/9.6/main/pg_hba.conf && \  
sed -i "s/#listen_addresses =.*/listen_addresses = \'*\'/"
/etc/postgresql/9.6/main/postgresql.conf  

