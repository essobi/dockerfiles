FROM willhallonline/phpcs:2.9  
MAINTAINER Sami Hellsten "dropa@dropa.net"  
# Fetch Moodle Coding Standards  
RUN git clone git://github.com/moodlehq/moodle-local_codechecker.git
/root/moodlecs  
  
# Set Moodle as default CodeSniffer Standard  
RUN phpcs --config-set installed_paths /root/moodlecs  
RUN phpcs --config-set default_standard moodle  
  
WORKDIR /app  
  
CMD ["phpcs"]  
CMD ["phpcbf"]

