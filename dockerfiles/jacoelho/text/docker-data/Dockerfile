FROM debian:stable

RUN groupadd -g 1000 rails && \
  useradd -u 1000 -g rails rails && \
  mkdir -p /var/www/service/shared && \
  chown -R rails:rails /var/www/service/shared

VOLUME /var/www/service/shared

USER rails

CMD ["echo", "data container"]
