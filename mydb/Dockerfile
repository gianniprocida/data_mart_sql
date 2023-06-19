FROM mysql:8


COPY data_mart_airbnb.sql /docker-entrypoint-initdb.d/
COPY my.cnf /etc/mysql/conf.d

ENV MYSQL_ROOT_PASSWORD='example'

ENV MYSQL_DATABASE='datamart_airbnb'

# Set the MySQL server to bind to all network interfaces
ENV MYSQL_HOST=0.0.0.0


# Expose the default MySQL port
EXPOSE 3306

# Start the MySQL service
CMD ["mysqld"]

