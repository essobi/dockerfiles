from node:latest  
  
maintainer Alexander Schittler <a.schittler@77ps.de>  
  
add cacert.crt /tmp/cacert.crt  
add mozilla-bundle.crt /tmp/mozilla-bundle.crt  
run bash -c "cat /tmp/mozilla-bundle.crt /tmp/cacert.crt >
/etc/ssl/certs/mozilla-plus-cacert.crt"  
run update-ca-certificates  
run apt-get update  
run apt-get -y install ruby mysql-client  
run npm i -g grunt-cli karma-cli bower gulp-cli  
run gem install sass  
run npm config set registry https://registry.npmjs.eu/  

