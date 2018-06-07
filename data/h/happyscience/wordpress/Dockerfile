FROM wordpress  
MAINTAINER "ITMW" <team.info.itmw@happy-science.org>  
  
# Install packages  
RUN apt-get update && apt-get -y --force-yes -o Dpkg::Options::="--force-
confdef" install wget curl unzip python python-pip libapache2-mod-php5
php5-mysql php5-curl php5-gd vim locales && apt-get clean  
RUN pip install awscli  
  
# Generate locale  
RUN echo 'en_US.UTF-8 UTF-8' > /etc/locale.gen && locale-gen  
ENV LANGUAGE=en_US:en LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8  
# Install plugins  
COPY install-plugins.sh /  
RUN /install-plugins.sh  
  
EXPOSE 80  

