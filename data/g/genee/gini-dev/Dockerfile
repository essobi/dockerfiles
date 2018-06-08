FROM genee/gini:alpine  
MAINTAINER Jia Huang <iamfat@gmail.com>  
  
ENV GINI_ENV=development \  
SONAR_RUNNER_VERSION=3.0.1.733  
  
ADD pei /usr/local/share/pei  
  
# Install less and bash-completion and vim for easier use  
# Install XDebug  
# Install PHPUnit and PHP-CS-Fixer  
# Configure "git-up"  
# Install SonarQube Runner  
  
RUN apk update \  
&& apk add less bash bash-completion vim \  
&& pei xdebug \  
&& composer global require -q 'phpunit/phpunit:@stable' 'friendsofphp/php-cs-
fixer:@stable' 'behat/behat:@stable' 'phpspec/phpspec:@stable' \  
&& git config --global alias.up 'pull --rebase --autostash' \  
&& curl -sLo /etc/profile.d/git-prompt.sh \  
https://raw.githubusercontent.com/git/git/master/contrib/completion/git-
prompt.sh \  
&& apk add unzip openjdk8-jre \  
&& curl -skLo /tmp/sonar-scanner-${SONAR_RUNNER_VERSION}.zip \  
https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-
cli-${SONAR_RUNNER_VERSION}.zip \  
&& unzip /tmp/sonar-scanner-${SONAR_RUNNER_VERSION}.zip -d /tmp \  
&& rm /tmp/sonar-scanner-${SONAR_RUNNER_VERSION}.zip \  
&& mv /tmp/sonar-scanner-${SONAR_RUNNER_VERSION} /usr/local/share/sonar-
scanner \  
&& echo 'export PATH="/usr/local/share/sonar-scanner/bin:$PATH"' >>
/etc/profile.d/sonar-scanner.sh \  
&& rm -rf /var/cache/apk/*  
  

