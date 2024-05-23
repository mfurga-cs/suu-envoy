# contrib required for postgres plugin
FROM envoyproxy/envoy:contrib-v1.30.1

# install postgres
RUN apt update && \
	apt install -y --no-install-recommends postgresql

ENV PATH="${PATH}:/usr/lib/postgresql/14/bin"

ENV PGDATA=/var/lib/postgresql/data
USER postgres
RUN initdb

COPY ./init.sql /tmp/init.sql
RUN postgres & sleep 1 && psql < /tmp/init.sql

# start envoy in background (&)
# replace shell with postgres (exec)
CMD ["/bin/bash", "-c", "envoy -c /envoy.yaml & exec postgres"]
